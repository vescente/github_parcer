import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')