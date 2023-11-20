from bank_accounts import *

Mary = BankAccount(1000, "Mary")
# Jason = BankAccount(2000, "Jason")
# Mary.getBalance()
# Jason.getBalance()
# Mary.deposit(500)
# Jason.withdraw(3000)
# Jason.transfer(10000, Mary)

# Inheritance
# Olivia = interestRewardsAcct(1000, "Olivia")
# Olivia.getBalance()
# Olivia.deposit(100)
# Olivia.transfer(200, Mary)

Annie = SavingsAcct(1000, "Annie")
Annie.getBalance()
Annie.deposit(100)
# Annie.transfer(2000, Mary)
Annie.transfer(1000, Mary)

