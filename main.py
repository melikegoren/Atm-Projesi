import sqlite3 as sql
connect = sql.connect("ATMprojesi.db")
print('AtmProjesi.db dosyasi olusturuldu')
cursor = connect.cursor()
sqlite_select_Query = "select sqlite_version()"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
cursor.close()


connect.commit()
#connect.close()
