import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'parcer_result.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False