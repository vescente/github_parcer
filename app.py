from flask import Flask, render_template, request
from src.classifier import CodeClassifier
from src.config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


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
    code_classifier = CodeClassifier(repo_name)
    unsafe_modules = code_classifier.analyze_code()
    return render_template('results.html', unsafe_modules=unsafe_modules, repo_url=repo_url)


if __name__ == '__main__':
    app.run(debug=True)
