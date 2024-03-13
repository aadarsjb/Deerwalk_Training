class Bank:
    def __init__(self):
        self.accounts = {}
        self.intrest_rate = 0.12
        self.govt_holidays = ["2024-01-01", "2024-02-18"]

    def open_account(self, first_name, last_name, age, balance = 0):
        account_number = self.generate_account_number()
        account_info = {
            'firste_name' : first_name,
            'last_name' : last_name,
            'age' : age,
            'balance' : balance   
           }
        
        self.accounts[account_number] = account_info
        return account_number
    
    def generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(6)


    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            return "Account not Found"
        
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            return f"Deposited {amount} into account {account_number}."
        else:
            return " Account not found."
        

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                return f"Withdrawl {amount} from account {account_number}."
            else:
                return "Insufficent funds"
        else:
            return "Account not found."

    def is_govt_holiday(self):
        today = '2022-05-01'
        return today in self.govt_holidays

bank = Bank()

#Open an account
account_number = bank.open_account("Hari", "Subedi", 22, 10000)

#Check Balance
print(bank.check_balance(account_number))

#Deposit money
print(bank.deposit(account_number, 500))

# check balance
print(bank.check_balance(account_number))

# Withdraw money
print(bank.withdraw(account_number, 200))

# Check if it's a government holiday
print(bank.is_govt_holiday())
















