import os

db_path = './src/db/parcer_result.db'
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"База данных {db_path} удалена.")
else:
    print(f"База данных {db_path} не существует.")


from src.models import db
from app import app

with app.app_context():
    db.create_all()
    print("Новая база данных создана.")