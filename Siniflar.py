from abc import ABC , abstractmethod
from enum import Enum
from datetime import datetime #işlemlerşn yapıldığı tarihi çekmek için import edildi
import sqlite3 as sql


connect = sql.connect('ATMprojesi.db')
crsr = connect.cursor()
komut=''

class TransactionStatus(Enum):
    SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE = 1, 2, 3, 4, 5, 6


class CustomerStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, CLOSED, UNKNOWN = 1, 2, 3, 4, 5, 6, 7

class Account():
    def __init__(self, account_number):
        self.__account_number = account_number
        komut=f"SELECT ID,AVAILABLE_BALANCE, TOTAL_BALANCE FROM ACCOUNT WHERE ACCOUNT_NUMBER= '{str(self.__account_number)}'"
        crsr.execute(komut)
        balance=crsr.fetchone()
        self.__account_id=balance[0]
        self.__available_balance=balance[1]
        self.__total_balance=balance[2]
   
    def get_account_id(self):
        return self.__account_id

    def get_available_balance(self):
        return self.__available_balance

    def get_total_balance(self):
        return self.__total_balance

class SavingAccount(Account):
    def __init__(self):
        komut="SELECT WITHDRAW_LIMIT FROM ACCOUNT WHERE ACCOUNT_NUMBER="+str(super().get_account_number(acc1)) ## acc1 oluşturulan account nesnesinin ismi##
        crsr.execute(komut)
        self.__withdraw_limit = crsr.fetchone()

    def get_withdraw_limit(self):
        return self.__withdraw_limit[0]

    #####customer classı sadece status almak için kullanılacak#####
class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        #self.__card = Card()
        #self.__account = Account()
    
    def make_transaction(self, transaction):
        None

    def get_status(self):
        return self.__status

    def get_billing_address(self):
        None

        ######transaction lar #########
class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_date(self):
        return self.__creation_time

    def get_transaction_status(self):
        return self.__status

    @abstractmethod
    def make_transation(self):
        None



class Deposit(Transaction):##cash ve check depositte super().__init__(amount) ile deposit oluşturulacağı için ekstra deposit oluturmaya gerek yok
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def make_transation(self):
        None

class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id

    def get_account_id(self):
        return self.__account_id

    def make_transation(self):
        total_balance= Account.get_total_balance(acc1) #acc1, Account classından oluşturulacak olan nesnenin adı.
        return total_balance

class CashDeposit(Deposit):
    def __init__(self, amount,cash_deposit_limit):
        super().__init__(amount)
        self.__cash_deposit_limit = cash_deposit_limit

    def make_transation(self):
        if Customer.get_status(cus1)==1:
            if self.__cash_deposit_limit>= super().get_amount():
                komut="insert into CASH_DEPOSIT (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) values ("+ str(super().get_amount()) +", 1, '"+ str(datetime.now()) +"',"+ Account.get_account_id(acc1) +", 1)"
                crsr.execute(komut)
                connect.commit()
            else:
                komut="insert into CASH_DEPOSIT (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) values ("+ str(super().get_amount()) +", 2, '"+ str(datetime.now()) +"',"+ Account.get_account_id(acc1) +", 1)"
                crsr.execute(komut)
                connect.commit()
        else:
            komut="insert into CASH_DEPOSIT (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) values ("+ str(super().get_amount()) +", 2, '"+ str(datetime.now()) +"',"+ Account.get_account_id(acc1) +", 1)"
            crsr.execute(komut)
            connect.commit()

class CheckDeposit(Deposit):
    def __init__(self, amount,check_number, bank_code):
        super().__init__(amount)
        self.__check_number = check_number
        self.__bank_code = bank_code

    def get_check_number(self):
        return self.__check_number

    def make_transation(self):
        if Customer.get_status(cus1)==1:
            komut="insert into CHECK_DEPOSIT(AMOUNT, CHECK_NUMBER, BANK_CODE, STATUS,_DATE, ACCOUNT_ID, ATM_ID) values(200, "+ str(self.__check_number) +", "+ str(self.__bank_code) +", 1, '"+ str(datetime.now()) +"',"+ Account.get_account_id(acc1) +", 1)"
            crsr.execute(komut)
            connect.commit()
        else:
            komut="insert into CHECK_DEPOSIT(AMOUNT, CHECK_NUMBER, BANK_CODE, STATUS,_DATE, ACCOUNT_ID, ATM_ID) values(200, "+ str(self.__check_number) +", "+ str(self.__bank_code) +", 2, '"+ str(datetime.now()) +"',"+ Account.get_account_id(acc1) +", 1)"
            crsr.execute(komut)
            connect.commit()

class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def make_transation(self):
        if Customer.get_status(cus1)==1:
            if Account.get_available_balance(acc1) >= self.__amount:
                if SavingAccount.get_withdraw_limit(sa1)>=self.__amount:###sa1, savingaccount nesnesinin ismi
                    #new_limit=SavingAccount.get_withdraw_limit(sa1)-self.__amount   ## para çekmekten sonra  çekim limiti ve total_balance düzenlenmeli fakat nasıl olacağını bilmiyorum
                    komut="INSERT INTO WITHDRAW (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) VALUES("+str(self.__amount)+",1,'"+str(datetime.now()) +"',"+ Account.get_account_id(acc1) +",1)"
                    crsr.execute(komut)
                    connect.commit()
                else:
                    komut="INSERT INTO WITHDRAW (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) VALUES("+str(self.__amount)+",2,'"+str(datetime.now()) +"',"+ Account.get_account_id(acc1) +",1)"
                    crsr.execute(komut)
                    connect.commit()
            else:
                komut="INSERT INTO WITHDRAW (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) VALUES("+str(self.__amount)+",2,'"+str(datetime.now()) +"',"+ Account.get_account_id(acc1) +",1)"
                crsr.execute(komut)
                connect.commit()
        else:
            komut="INSERT INTO WITHDRAW (AMOUNT, STATUS, _DATE, ACCOUNT_ID, ATM_ID) VALUES("+str(self.__amount)+",2,'"+str(datetime.now()) +"',"+ Account.get_account_id(acc1) +",1)"
            crsr.execute(komut)
            connect.commit()
##########transaction sonu######################################

 #####account nesnesi oluşturma ######################      
#customer_pin = "1234"
#komut = f"select ACCOUNT_NUMBER from ACCOUNT where ID=(select ACCOUNT from CUSTOMER where ID=(select CUSTOMER_ID from CARD where PIN = '{str(customer_pin)}' )) "
#crsr.execute(komut)
#acc_number=crsr.fetchone()
#acc1 = Account(acc_number[0])
#komut=f"select NAME,E_MAIL,PHONE,ADDRESS,STATUS from CUSTOMER where ACCOUNT='{(str(acc1.get_account_id()))}'"
#crsr.execute(komut)
#customer = crsr.fetchall()
#print(customer[0][0])
#cus1 = Customer(customer[0][0], customer[0][1], customer[0][2], customer[0][3], customer[0][4])

################################