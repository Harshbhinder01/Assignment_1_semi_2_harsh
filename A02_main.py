"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), -100.00, 0.05)

# 3. Print the ChequingAccount created in step 2.
print(chequing)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"service charges:${chequing.get_service_charges(),2}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
chequing.deposit(60.00)
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
print(chequing)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service charge after the deposit: $ {round(chequing.get_service_charges(), 2)}")


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
saving = SavingsAccount(1020, 12, 100.00, date(2025, 2, 15), 50.00)


# 6. Print the SavingsAccount created in step 5.
print(saving)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service charges: $ {round(saving.get_service_charges(), 2)}")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
saving.withdraw(80.00)
# 7b. Print the SavingsAccount.
print(saving)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service charge after the withdraw: $ {round(saving.get_service_charges(), 2)}")




print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment = InvestmentAccount(1020, 12, 50.00, date(2022, 2, 15), 2.00)


# 9a. Print the InvestmentAccount created in step 8.
print(investment)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service charge: $ {round(investment.get_service_charges(), 2)}")


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
prior_investment = InvestmentAccount(1020, 12, 50.00, date(2005, 2, 15), 2.00)



# 11a. Print the InvestmentAccount created in step 10.
print(prior_investment)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service charge: $ {round(prior_investment.get_service_charges(), 2)}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing.withdraw(chequing.get_service_charges())
saving.withdraw(saving.get_service_charges())
investment.withdraw(investment.get_service_charges())
prior_investment.withdraw(prior_investment.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("updated bank info:")
print("chequing account after service charges")
print(chequing)
print("savings account after service charges")
print(saving)
print("investment account created within the last ")
print(investment)
print("investment account created more than 10 years ago")
print(prior_investment)
