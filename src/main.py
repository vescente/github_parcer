import json
from github_api import search_repositories
from classifier import CodeClassifier
from config import SQLALCHEMY_DATABASE_URI
from models import db, Repository, AnalysisResult
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def analyze_repository(repo_full_name, keywords):
    print(f"Analyzing repository: {repo_full_name}")
    code_classifier = CodeClassifier(repo_full_name)
    unsafe_modules = code_classifier.analyze_code()
    return {
        'url': f'https://github.com/{repo_full_name}',
        'words': keywords,
        'unsafe_modules': unsafe_modules
    }


def main():
    with app.app_context():
        db.create_all()

        choice = input(
            "Do you want to search by keywords or enter a specific repository URL? (keywords/url): ").strip().lower()
        results = {}

        if choice == 'keywords':
            keywords = input(
                "Enter keywords to search for repositories (comma-separated): ").split(',')
            for keyword in keywords:
                keyword = keyword.strip()
                print(f"Searching for repositories with keyword: {keyword}")
                repos = search_repositories(keyword)

                for repo in repos:
                    repo_results = analyzгe_repository(
                        repo['full_name'], [keyword])
                    results[repo_results['url']] = {
                        'words': repo_results['words'],
                        'unsafe_modules': repo_results['unsafe_modules']
                    }

                    # Сохранение информации о репозитории
                    repository = Repository(url=repo_results['url'])
                    db.session.add(repository)
                    db.session.commit()
                    print(
                        f"Repository {repository.url} saved with ID {repository.id}")

                    # Сохранение результатов анализа в базу данных
                    for module in repo_results['unsafe_modules']:
                        result = AnalysisResult(
                            repo_id=repository.id,
                            file_name=module['name'],
                            unsafe_code_type=module['unsafe code type'],
                            status=module['status']
                        )
                        db.session.add(result)
                    db.session.commit()
                    print(f"Analysis results for {repository.url} saved")

        elif choice == 'url':
            repo_url = input(
                "Enter the repository URL (e.g., owner/repo): ").strip()
            repo_results = analyze_repository(repo_url, [])
            results[repo_results['url']] = {
                'words': repo_results['words'],
                'unsafe_modules': repo_results['unsafe_modules']
            }

            # Сохранение информации о репозитории
            repository = Repository(url=repo_results['url'])
            db.session.add(repository)
            db.session.commit()
            print(f"Repository {repository.url} saved with ID {repository.id}")

            # Сохранение результатов анализа в базу данных
            for module in repo_results['unsafe_modules']:
                result = AnalysisResult(
                    repo_id=repository.id,
                    file_name=module['name'],
                    unsafe_code_type=module['unsafe code type'],
                    status=module['status']
                )
                db.session.add(result)
            db.session.commit()
            print(f"Analysis results for {repository.url} saved")

        else:
            print("Invalid choice. Please enter 'keywords' or 'url'.")
            return

        # Запись результатов в файл results.json
        try:
            with open('results.json', 'w') as json_file:
                json.dump(results, json_file, indent=4)
            print("Analysis complete. Results saved to results.json.")
        except Exception as e:
            print(f"Error writing to results.json: {e}")


if __name__ == "__main__":
    main()
