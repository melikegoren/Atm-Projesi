import sqlite3 as sql
connect = sql.connect('deneme.db')
print('deneme dosyasi olusturuldu')
cursor = connect.cursor()
print('cursor olusturuldu')

cursor.execute(""" CREATE TABLE IF NOT EXISTS STUDENTS(
    name text,
    lastname text,
    age integer)
""")
cursor.execute(""" INSERT INTO STUDENTS VALUES('Melike', 'Gören', 22)
""")

connect.commit()
#connect.close()
