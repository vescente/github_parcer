import sqlite3

def check_records():
    conn = sqlite3.connect('./src/db/parcer_result.db')
    cursor = conn.cursor()

    # Проверить, что есть записи в таблице repositories
    cursor.execute("SELECT COUNT(*) FROM repositories")
    repo_count = cursor.fetchone()[0]
    if repo_count > 0:
        print("Есть записи в таблице repositories")
    else:
        print("Нет записей в таблице repositories")

    # Проверить, что есть записи в таблице analysis_results
    cursor.execute("SELECT COUNT(*) FROM analysis_results")
    analysis_count = cursor.fetchone()[0]
    if analysis_count > 0:
        print("Есть записи в таблице analysis_results")
    else:
        print("Нет записей в таблице analysis_results")

    conn.close()

check_records()