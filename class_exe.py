class Bank:
    #private variable
    __intrest_rate = 12

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = 0

    def get_balance(self):
        return self.__balance
    
    def deposit_balance(self, deposit_amount):
        self.__balance = self.__balance + deposit_amount

    def withdraw_balance(self, withdrawl_amount):
        self.__balance = self.__balance - withdrawl_amount

    @classmethod
    def get_intrest_rate(cls):
        return cls.__intrest_rate

    @classmethod
    def set_intrest_rate(cls, new_rate):
        cls.__intrest_rate = new_rate

    @staticmethod
    def print_govt_holiday():
        print('Dashain Holiday')
        print('Tihar Holiday')

account = None













