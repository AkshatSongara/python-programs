class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
print(account.get_balance())

account.__balance = 6000
print(account.get_balance())