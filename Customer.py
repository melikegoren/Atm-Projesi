class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        #self.__card = Card()
        #self.__account = Account

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def get_address(self):
        return self.__address

    @get_address.setter
    def set_name(self, address):
        self.__address = address

    @property
    def get_email(self):
        return self.__email

    @get_email.setter
    def set_email(self, email):
        self.__email = email

    @property
    def get_phone(self):
        return self.__phone

    @get_phone.setter
    def set_phone(self,phone):
        self.__phone = phone

    @property
    def get_status(self):
        return self.__status

    @get_status.setter
    def set_status(self, status):
        self.__status = status






    def make_transaction(self, transaction):
        None

    def get_billing_address(self):
        None