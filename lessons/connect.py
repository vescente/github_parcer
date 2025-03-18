import sqlite3

conn = sqlite3.connect('.\db\hh.sqlite')

cursor = conn.cursor()


# cursor.execute('select * from region where name = ?', ('Moscow',))
# result = cursor.fetchall()
# print(cursor.fetchall())

# for item in result:
#     print(item)

cursor.execute(
    'insert into vacancykey_skills (vacancy_id,key_skill_id) values (?, ?)', (1, 5))


cursor.execute('select * from vacancykey_skills')
print(cursor.fetchall())


# exit
conn.commit()