from flask import Flask, render_template, request
from src.classifier import CodeClassifier
from src.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from src.models import db, Repository, AnalysisResult
import json  # Импортируем модуль json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Проверка существования базы данных и таблиц
with app.app_context():
    db_path = os.path.join('src', 'db', 'parcer_result.db')
    if not os.path.exists(db_path):
        db.create_all()
        print("База данных и таблицы созданы.")
    else:
        print("База данных уже существует.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/search', methods=['POST'])
def search():
    repo_url = request.form['repo_url']
    repo_name = repo_url.split('github.com/')[-1]
    print(f"Analyzing repository: {repo_name}")
    code_classifier = CodeClassifier(repo_name)
    unsafe_modules = code_classifier.analyze_code()
    print(f"Unsafe modules found: {unsafe_modules}")

    # Сохранение информации о репозитории
    try:
        repository = Repository.query.filter_by(url=repo_url).first()
        if not repository:
            repository = Repository(url=repo_url)
            db.session.add(repository)
            db.session.commit()
            print(f"Repository {repository.url} saved with ID {repository.id}")
        else:
            print(f"Repository {repository.url} already exists with ID {repository.id}")
    except Exception as e:
        print(f"Error saving repository: {e}")
        db.session.rollback()

    # Сохранение результатов анализа в базу данных
    try:
        for module in unsafe_modules:
            result = AnalysisResult(
                repo_id=repository.id,
                file_name=module['name'],
                unsafe_code_type=module['unsafe code type'],
                status=module['status']
            )
            db.session.add(result)
        db.session.commit()
        print(f"Analysis results for {repository.url} saved")
    except Exception as e:
        print(f"Error saving analysis results: {e}")
        db.session.rollback()

    # Запись результатов в файл results.json
    results = {
        repo_url: {
            'words': [],
            'unsafe_modules': unsafe_modules
        }
    }
    try:
        with open('results.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
        print("Analysis complete. Results saved to results.json.")
    except Exception as e:
        print(f"Error writing to results.json: {e}")

    return render_template('results.html', unsafe_modules=unsafe_modules, repo_url=repo_url)

if __name__ == '__main__':
    app.run(debug=True)