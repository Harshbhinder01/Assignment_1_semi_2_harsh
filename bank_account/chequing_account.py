from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

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

        self._strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

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
        this function will call the calculate service charge 
        """
        return self._strategy.calculate_service_charges(self)
        
    def __str__(self) -> str:
        """
        this is the formatted str.
        """
        main_str = super().__str__()
        return (f"{main_str}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} "
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing")
    




        

    

