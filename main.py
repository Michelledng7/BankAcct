from bank_accounts import *

Mary = BankAccount(1000, "Mary")
Jason = BankAccount(2000, "Jason")
Mary.getBalance()
Jason.getBalance()
Mary.deposit(500)
Jason.withdraw(3000)
Jason.transfer(10000, Mary)
