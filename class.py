class Bank:
    
    __intrest_rate = 12

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = 0

    
    def check_balance(self):
        return self.__balance
    
    def deposite_balance(self, deposite_amount):
        self.__balance = self.__balance + deposite_amount

    
    def withdraw_balance(self, withdrawl_amount):
        self.__balance = self.__balance - withdrawl_amount

    @classmethod
    def get_intrest_rate(cls):
        return cls.__intrest_rate
    
    @classmethod
    def set_intrest_rate(cls, new_rate):
        cls.__intrest_rate = new_rate

    @staticmethod
    def print_govt_holidays():
        print('Dashain holiday')
        print('Tihar holiday')

while True:

    fn = input('Enter first Name')
    ln = input('Enter last name')






































    










