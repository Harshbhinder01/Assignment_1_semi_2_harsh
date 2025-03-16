from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

        self._strategy = MinimumBalanceStrategy(minimum_balance)
        
    @property
    def minimum_balance(self) -> float:
        """
        this returns the minimum balance
        """
        return self.__minimum_balance
    
    
    def __str__(self) -> str:
        """
        this shows a string representation
        """
        return (super().__str__() +
                f"\nMinimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")
    
    def get_service_charges(self):
        """
        if balance of the savings account is greater or equal to the minimum balance,
        then the service is set to the base service charge value.
        if the balance of the savings account is less than the minimum balance,
        then the service charge is calculated using using the formula.
        """
        return self._strategy.calculate_service_charges(self)
