class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid Balance.")

account = BankAccount(5000)
print("Initial Account Balance:", account.balance)

account.balance = 10000
print("Account Balance After Changed:", account.balance)