import sqlite3 as sql
import tkinter as tk
from tkinter import *
import random as rand


from Siniflar import Account
connect = sql.connect("ATMprojesi.db")
print('AtmProjesi.db dosyasi olusturuldu')
cursor = connect.cursor()
#connect.commit()
count = 0



def move_to_next_page():  #frame değiştirme fonksiyonu
    global count

    if not count > len(pages) - 2:

        for p in pages:
            p.pack_forget()

        count += 1
        page = pages[count]
        page.pack(pady=100)

result_show = ""
result2_show = ""
def show(symbol, char): #butondan aldığı değeri labela gönderecek
    global result_show
    global result2_show
    result_show += symbol
    result2_show += char
    invisible_pin_label.config(text=result2_show, background="white")
    pin_label.config(text=result_show)


def clear(): #labeldaki girilenleri sil
    global result_show
    global result2_show
    pin_label.config(text="")
    invisible_pin_label.config(text="")
    result_show = ""
    result2_show = ""



def delete(): #labeldaki bütün değerleri sil (page2)
    global result_show
    global result2_show
    #result_delete = pin_label.cget("text")
    pin_label.config(text=result_show[0:len(result_show)-1])
    invisible_pin_label.config(text=result2_show[0: len(result2_show)-1])
    result_show = result_show[0: len(result_show)-1]
    result2_show = result2_show[0: len(result2_show)-1]

def cancel(): #page2 exit
    exit()


def get_pin():
    password = invisible_pin_label.cget("text")
    komut_pin = "SELECT PIN FROM CARD"
    cursor.execute(komut_pin)
    pins = cursor.fetchall()
    customer_pin = pins[0]
    return str(customer_pin[0])
def check_pin(): #kullanıcının girdiği pini veritabanındakiler ile kontrol edip kullanıcıyı ana menüye yollayacak

    global page3
    check = False
    password = invisible_pin_label.cget("text")
    komut_pin = "SELECT PIN FROM CARD"
    cursor.execute(komut_pin)
    pins = cursor.fetchall()
    global customer_pin
    customer_pin = pins[0]
    print(customer_pin)



    print((pins[0]))
    print(password)


    for i in range(0,len(pins)):
        for j in range(i, len(pins)):
            if(pins[i][j] == password):
                check = True
                invisible_pin_label_page3 = tk.Label(page3, width=10, height=1, background="red",text=password)

                return  move_to_next_page()


    print(check)
    if(check == False):
        invalid_pin_screen = tk.Tk()
        invalid_pin_screen.geometry("300x300")
        invalid_label = tk.Label(invalid_pin_screen,text="Geçersiz Pin", width=50, height=5, background="red")
        invalid_label.pack()

    random_atm = rand.randint(1, 3)
    komut_atm_getir = f"SELECT ID FROM ATM WHERE ID = '{random_atm}'"
    cursor.execute(komut_atm_getir)
    global atm
    atm = cursor.fetchall()
    print(atm[0][0])

def page_kalan_bakiye():

    page4 = tk.Tk()
    page4.geometry("500x500")
    text_kalan_bakiye = f"Kalan bakiyeniz: {customer_account.get_total_balance()} "
    label_kalan_bakiye = tk.Label(page4, width=20, height=3, background="red", text=text_kalan_bakiye).grid(row=0, column=3, padx=180, pady=100)
    label_kalan_bakiye.grid(row=4, column=1, padx=50, pady=30)

    page3.pack_forget()

    #button_geri_gel = tk.Button(page4, text="Geri Dön", width=10,height=2).place(anchor=CENTER)


def page_para_cekme():
    page5 = tk.Tk()
    page5.geometry("500x500")







root = tk.Tk()
root.geometry("500x500")
page1 = tk.Frame(width=500,height=500)
button = tk.Button(page1, text="Kartınızı giriniz", height=2, width=15, command=move_to_next_page)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
page1.pack()
######################################################################
page2 = tk.Frame(width=800, height=800)
pin_label = tk.Label(page2, width=23, height=2, background="grey",padx=15, pady=15)
keypad_frame = tk.Frame(page2, width=800, height=200, padx=15, pady=30)
invisible_pin_label = tk.Label(page2, width=10, height=1, background="white")

Button(keypad_frame, text="1", width=5, height=2, command=lambda: show("*","1")).grid(row=0, column=0)
Button(keypad_frame, text="2", width=5, height=2, command=lambda: show("*","2")).grid(row=0, column=1)
Button(keypad_frame, text="3", width=5, height=2, command=lambda: show("*","3")).grid(row=0, column=2)
Button(keypad_frame, text="4", width=5, height=2, command=lambda: show("*","4")).grid(row=1, column=0)
Button(keypad_frame, text="5", width=5, height=2, command=lambda: show("*","5")).grid(row=1, column=1)
Button(keypad_frame, text="6", width=5, height=2, command=lambda: show("*","6")).grid(row=1, column=2)
Button(keypad_frame, text="7", width=5, height=2, command=lambda: show("*","7")).grid(row=2, column=0)
Button(keypad_frame, text="8", width=5, height=2, command=lambda: show("*","8")).grid(row=2, column=1)
Button(keypad_frame, text="9", width=5, height=2, command=lambda: show("*","9")).grid(row=2, column=2)
Button(keypad_frame, text="0", width=5, height=2, command=lambda: show("*","0")).grid(row=3, column=1)
Button(keypad_frame, text="İptal", width=7, height=2, command=lambda: clear()).grid(row=0, column=3)
Button(keypad_frame, text="Sil", width=7, height=2, command=lambda: delete()).grid(row=1, column=3)
Button(keypad_frame, text="Kapat",width=7, height=2, command=lambda: exit()).grid(row=2, column=3)

Button(keypad_frame, text="Giriş", width=7, height=2, command=lambda: [check_pin(), get_pin()]).grid(row=3,column=3)


pin_label.grid(row=0,column=0)
keypad_frame.grid(row=2, column=0)






page2.pack()
###########################################################################################
page3 = tk.Frame(root,width=500, height=1000,background="grey")
text_hosgeldiniz = "HOŞGELDİNİZ"
label_hosgeldiniz = tk.Label(page3, width=30, height=3, background="grey", text=text_hosgeldiniz, font="bold")
label_hosgeldiniz.grid(row=0,column=0,padx=50, pady=1)
button_deposit = tk.Button(page3, width=10, height=2,background="white", text="Para Yatırma",highlightthickness=3, highlightbackground="blue")
button_deposit.grid(row=1, column=0, padx=50,pady=2)
button_withdraw = tk.Button(page3, width=10, height=2, background="white", text="Para Çekme",highlightthickness=3, highlightbackground="blue")
button_withdraw.grid(row=2, column=0, padx=50, pady=3)
button_transfer = tk.Button(page3, width=10, height=2, background="white", text="Para Transferi",highlightthickness=3, highlightbackground="blue")
button_transfer.grid(row=3, column=0, padx=50, pady=4)
button_balance_inquiry = tk.Button(page3, width=10, height=2, background="white", text="Kalan Bakiye", command=lambda: page_kalan_bakiye(),highlightthickness=3, highlightbackground="blue")
button_balance_inquiry.grid(row=4,column=0, padx=50, pady=5)

pin_code = get_pin()
print(f"pin code: {pin_code} ")
komut_account_getir = f"SELECT ACCOUNT_NUMBER FROM ACCOUNT WHERE ID = (SELECT ACCOUNT FROM CUSTOMER WHERE ID = (SELECT CUSTOMER_ID FROM CARD WHERE PIN = '{str(get_pin())}')) "
cursor.execute(komut_account_getir)
account = cursor.fetchall()
account_number = account[0]
print(account_number)
customer_account = Account((account_number[0]))
print(customer_account.get_account_id())




page3.pack()
###############################################################

pages = [page1, page2, page3]



root.mainloop()



cursor.close()

#connect.close()
