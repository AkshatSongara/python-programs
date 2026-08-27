class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account = BankAccount(5000)
print("Account Balance:", account.balance)

account.balance = -10000
print("Account Balance:", account.balance)