class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initAmount, acctName):
        self.balance = initAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit successful.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
                (
                    f"Sorry, account {self.name} has only a balance of ${self.balance:.2f}")
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal successful.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print(
                f"\n**********Transfering ${amount: .2f} to {account.name} **********")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer successful.********** ✅\n")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error} ❌")
