class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(5000)
print("Initial account balance:", account.get_balance())

account.deposite(4000)
print("Balance after deposite:", account.get_balance())