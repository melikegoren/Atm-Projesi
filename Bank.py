from abc import ABC
import sqlite3 as sql

connect = sql.connect("ATMprojesi.db")
cursor = connect.cursor()




class Bank:
    def __init__(self, name, bank_code):

        self.__name = name
        self.__bank_code = bank_code


    def get_bank_code(self):
        return self.__bank_code


    #farklı lokasyona atm ataması yapılabilir.
    def add_atm(self):
        komut2 = "INSERT INTO ATM (LOCATION, TOTAL_FIVE_DOLLAR_BILLS, TOTAL_TWENTY_DOLLAR_BILLS) VALUES (1,500,300)"
        cursor.execute(komut2)
        connect.commit()



    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self,name):
        self.__name = name


komut = "SELECT NAME,BANK_CODE from BANK"
cursor.execute(komut)
veri = cursor.fetchone()
name = str(veri[0])
bank_code = str(veri[1])


a = Bank(name, bank_code)
print(a.get_bank_code())

a.add_atm()


