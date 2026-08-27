class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
print("Initial account balance:", account.get_balance())

account.deposite(10000)
print("Account balance after deposite:", account.get_balance())

account.withdraw(4000)
print("Account balance after withdrawal:", account.get_balance())