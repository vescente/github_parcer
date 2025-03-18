import requests
from src.config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com"


def search_repositories(keyword, per_page=30, page=1):
    """
    Search repositories on GitHub based on a keyword.
    kayword sample: "python"
    """
    url = f"{GITHUB_API_URL}/search/repositories"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    params = {
        "q": keyword,
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()['items']


def get_repository_contents(owner, repo, path=""):
    """
    get the contents of a repository on GitHub.
    owner: the owner of the repository
    repo: the repository name
    """
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_code_snippets(owner, repo):
    """
    get code snippets from a repository on GitHub.
    owner: the owner of the repository
    repo: the repository name
    """
    contents = get_repository_contents(owner, repo)
    code_snippets = []
    for item in contents:
        if item['type'] == 'file' and item['name'].endswith(('.py', '.js', '.java')):
            code_snippets.append(
                get_repository_contents(owner, repo, item['path']))
    return code_snippets