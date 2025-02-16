from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):

        # calling the superclass constructor
        super().__init__(account_number, client_number, balance, date_created)
        
        
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.00

        
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

    @property
    def overdraft_limit(self) -> float:
        """ this returns the overdraft limit"""
        return self.__overdraft_limit
    
    @property
    def overdraft_rate(self) -> float:
        """ this returns the overdraft rate"""
        return self.__overdraft_rate
    
    def get_service_charges(self):
        """
        if the balance of the chequing account is greater than or equal to the overdraft limit ,
        then the service charge is set to the base service charge value 
        if the balance of the chequing account is less than the overdraft limit, 
        then the service charge is calculated using the formula.
        """
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        
    def __str__(self) -> str:
        """
        this is the formatted str.
        """
        return (super().__str__() +
                f"\nOverdraft Limit: ${self.__overdraft_limit:,.2f}" +
                f"\nOverdraft Rate: {self.__overdraft_rate * 100:.2f}" +
                "\nAccount Type: Chequing")
        
    




        

    

