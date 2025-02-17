from datetime import date

class BankAccount:
    BASE_SERVICE_CHARGE: float = 0.50 # this is a constant for the base service charge that is a float.
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date ):
        """
        args:
        account_number: An integer value representing the bank account number
        client_number: An integer value representing the client number representing the account holder
        balance: A float value representing the current balance.
        date_created: the date the account was created.

        ValueErrors:
        account_number: if the value is not int raise a ValueError.
        client_number: if the value is not a int raise a ValueError.
        balance: if the value is not a float raise a ValueError.
        date_created: if the date created is not vald it will default to todays date
        """
        #if the value is not int raise a ValueError.
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("The account number must be a int") 
        
        #if the value is not a int raise a ValueError.
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("the client number must be a int")
        
        #if the value is not a float raise a ValueError.
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0
        
        # if the date_created is not valid default to todays date
        if isinstance(date_created, date):
            self.__date_created = date_created 
        else:
            self.__date_created = date.today()

    @property
    def account_number(self) -> int:
        """
        this returns the account number
        """
        return self.__account_number
    
    @property
    def client_number(self) ->int:
        """
        this returns the client number
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        this returns the current balance of the account
        """
        return self.__balance
    
    @property
    def date_created(self) -> date:
        """
        this returns the date
        """
        return self.__date_created
    
    def update_balance(self, amount:float):
        """
        this updates the balance if the balance is invalid it will raise a valueerror
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            print("this is a invalid amount")
        
    def deposit(self, amount):
        if not isinstance(amount, (int,float)):
            raise ValueError(f"deposit amount: {amount} must be a numeric")
        if amount <=0:
            format_amount = f"{amount:,.2f}"
            raise ValueError(f"deposit amount:{format_amount} must be a positive")
        
        self.update_balance(amount)

    def withdraw(self, amount):
        if not isinstance(amount, (int,float)):
            raise ValueError(f"withdraw amount: {amount} must be a numeric")
        
        if amount <=0:
            format_amount = f"{amount:,.2f}"
            raise ValueError(f"withdraw amount:{format_amount} must be a positive")
        
        if amount > self.__balance:
            format_balance = f"{self.__balance:,.2f}"
            format_amount = f"{amount:,.2f}"
            raise ValueError(f"withdraw amount: {format_amount} cannot exceed the account balance: {format_balance}")
        
        self.update_balance(amount)

    def __str__(self) -> str:
        """
        this is the formatted str.
        """
        formatted_balance = f"${self.__balance}"
        return f"Account Number: {self.__account_number} Balance: {formatted_balance}"

    def get_service_charges(self) -> float:
        """ this will return the service charge"""
        return self.BASE_SERVICE_CHARGE

            
    
        

        


    
        

        
