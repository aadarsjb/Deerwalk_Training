class Bank:
    
    __intrest_rate = 12

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = 0

    
    def get_balance(self):
        return self.__balance
    
    def deposit_balance(self, deposite_amount):
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

account = None
while True:

    choice = input('Enter 1 to create account. \nEnter 2 to check balance. \nEnter 3 to deposit balance. \nEnter 5 to withdraw balance. \nEnter 6 to change intrest rate. \nEnter 7 to get holidays.')

    if choice == '1':
        fn = input('Enter first name: ')
        ln = input('Enter last name: ')

        account = Bank(first_name = fn, last_name=ln)

        print('Account has been created successfully')

    elif choice == '2':
        account.get_balance()

    elif choice == '3':
        deposit_amount = float(input('Enter deposit amount: '))
        account.deposit_balance(deposit_amount)

    elif choice == '4':
        withdrawl_amount = int(input('Enter withdrawl amount: '))

































    










