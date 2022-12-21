import sqlite3 as sql
import tkinter as tk
from tkinter import CENTER

connect = sql.connect("ATMprojesi.db")
print('AtmProjesi.db dosyasi olusturuldu')
cursor = connect.cursor()
#sqlite_select_Query = "select sqlite_version()"
#cursor.execute(sqlite_select_Query)
#record = cursor.fetchall()
#print("SQLite Database Version is: ", record)
connect.commit()
count = 0
def move_to_next_page():
    global count

    if not count > len(pages) - 2:

        for p in pages:
            p.pack_forget()

        count += 1
        page = pages[count]
        page.pack(pady=100)

root = tk.Tk()
root.geometry("500x500")
page1 = tk.Frame(width=500,height=500)
button = tk.Button(root, text="Kartınızı giriniz", height=2, width=15, command=move_to_next_page)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
page1.pack()
page2 = tk.Frame(width=500,height=500)
pages = [page1, page2]


root.mainloop()





cursor.close()



#connect.close()
