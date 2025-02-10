""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    client = None
    try:
        client = Client (100, "harsh", "bhinder", "harshbhinder@pixel.com")
        print(f"Client created successfully: {client}")
    except ValueError:
        print("ran into error while creating the info for the client")



    # 2. Declare a BankAccount object with an initial value of None.
    Bank_Account = None
 

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        Bank_Account = BankAccount(1234, 22, 25.00)
        print(f"Bank account created successfully: {BankAccount}")
    except ValueError:
        print(f" Error for creating bank account")



    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try: 
        Bank_Account = BankAccount(1234, 22 ,"hb")
    except:
        print(f"Error while creating the bank account with invalid balance")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    if client:
        print(f"client: {client}")
    if Bank_Account:
        print(f"BankAccount: {Bank_Account}")



    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        Bank_Account.deposit("hb")
    except ValueError:
        print(f"Error while depositing a non-numeric value")


    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        Bank_Account.deposit(-50)
    except ValueError:
        print(f"Error while depositing a negative value")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    try:
        Bank_Account.withdraw(10)
        print(f" After withdrawal: {Bank_Account}")
    except ValueError:
        print(f"Error while withdrawing a valid amount")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        Bank_Account.withdraw("hb")
    except ValueError:
        print(f"Error while withdrawing a non-numeric value")


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        Bank_Account.withdraw(-30)
    except ValueError:
        print(f"Error while withdrawing a negative value")


    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        Bank_Account.withdraw(100)
    except ValueError:
        print(f"Error while withdrawing an amount that exx+eeds the balance")

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(f"Final BankAccount instance: {Bank_Account}")
  


if __name__ == "__main__":
 main()