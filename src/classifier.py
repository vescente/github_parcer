import requests
import base64
from config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com"


class CodeClassifier:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.unsafe_patterns = {
            'eval': 'Use of eval() can execute arbitrary code.',
            'exec': 'Use of exec() can execute arbitrary code.',
            'os.system': 'Use of os.system() can lead to command injection.',
            'subprocess': 'Improper use of subprocess can lead to command injection.',
            'SQL injection': 'Potential SQL injection vulnerability.',
            'Django insecure': 'Django-specific vulnerabilities detected.'
        }
        self.results = []

    def get_repository_contents(self, path=""):
        url = f"{GITHUB_API_URL}/repos/{self.repo_name}/contents/{path}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_code_snippets(self):
        contents = self.get_repository_contents()
        code_snippets = []
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith(('.py', '.js', '.java')):
                file_content = self.get_repository_contents(item['path'])
                code = base64.b64decode(
                    file_content['content']).decode('utf-8')
                code_snippets.append({'name': item['name'], 'code': code})
        return code_snippets

    def analyze_code(self):
        code_snippets = self.get_code_snippets()
        unsafe_modules = []
        for snippet in code_snippets:
            findings = []
            for pattern, message in self.unsafe_patterns.items():
                if pattern in snippet['code']:
                    findings.append(message)
            if findings:
                unsafe_modules.append({
                    'name': snippet['name'],
                    'unsafe code type': ', '.join(findings),
                    'status': 'Potentially unsafe' if 'Potential' in ', '.join(findings) else 'Contains vulnerability'
                })
        return unsafe_modules
