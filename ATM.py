class ATM:
    def __init__(self, id, location):
        self.__atm_id = id
        self.__location = location

        self.__cash_dispenser = CashDispenser()
        self.__screen = Screen()
        self.__printer = Printer()
        self.__check_deposit = CheckDeposit()
        self.__cash_deposit = CashDeposit


    def authenticate_user(self):
        None


    def make_transaction(self, customer, transaction):
        None



