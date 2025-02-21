import json
from github_api import search_repositories
from classifier import CodeClassifier
from config import GITHUB_TOKEN


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
                repo_results = analyze_repository(repo['full_name'], [keyword])
                results[repo_results['url']] = {
                    'words': repo_results['words'],
                    'unsafe_modules': repo_results['unsafe_modules']
                }

    elif choice == 'url':
        repo_url = input(
            "Enter the repository URL (e.g., owner/repo): ").strip()
        repo_results = analyze_repository(repo_url, [])
        results[repo_results['url']] = {
            'words': repo_results['words'],
            'unsafe_modules': repo_results['unsafe_modules']
        }

    else:
        print("Invalid choice. Please enter 'keywords' or 'url'.")
        return

    with open('results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print("Analysis complete. Results saved to results.json.")


if __name__ == "__main__":
    main()
