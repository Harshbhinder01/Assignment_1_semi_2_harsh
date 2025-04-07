"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client







# 2. Create a Client object with data of your choice.
client_object = Client(1436, "Harsh", "Bhinder", "Harshbhinder01@gmail.com")

print(f"Client Object Created: {client_object}")




# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.

chequing_account = ChequingAccount(1234, client_object.client_number, 1000.00, date.today(), -20.00, 0.01)
print(f"The chequing account has been created: {chequing_account}")

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

savings = SavingsAccount(1345, client_object.client_number, 2000.00, date.today(), 100.00)
print(f"the savings account has been created: {savings} ")





# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).

chequing_account.attach(client_object)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

savings.attach(client_object)



# 5a. Create a second Client object with data of your choice.

second_client = Client(100, "mandeep", "Bhinder", "Mandeep@gmail.com")

print(f"the second client has been created: {second_client}")
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_second = (122, second_client.client_number, 2000.00, date.today(), 100.00)

print(f"the second savings account has been created:{savings_second}")



# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

print("\nChequing account transactions:")
try:
    chequing_account.deposit(1001)
    print(f"Chequing Account: The deposit has been made.")
except Exception as e:
    print(f"Chequing account has a deposit error: {e}.")
       
try:
    chequing_account.withdraw(400)
    print(f"Chequing Account: the withdrawl has been made.")
except Exception as e:
    print(f"Chequing account withdrawl had an error: {e}.")        
   
try:
    chequing_account.withdraw(40000)
    print(f"Chequing Account: the withdrawl has been made.")
except Exception as e:
    print(f"Chequing account the withdrwal had an error: {e} .")      
   
   
print("\nSavings Account transactions:")
try:
    savings.deposit(1000)
    print(f"saving account: The deposit has been made.")
except Exception as e:
    print(f"saving account the deposit had an error: {e}.")
       
try:
    savings.withdraw(400)
    print(f"saving account: The withdrwal has been made.")
except Exception as e:
    print(f"saving account the withdrwal had an error: {e}.")        
   
try:
    savings.withdraw(34000)
    print(f"saving Account: the withdrwal has been made.")
except Exception as e:
    print(f"saving account the withdrawal had an error: {e} .")  

