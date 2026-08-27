class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
print("Initial Account Balance:", account.get_balance())

account.set_balance(7000)
print("Account Balance After Change:", account.get_balance())

account.set_balance(-100)
print("Account Balance:", account.get_balance())