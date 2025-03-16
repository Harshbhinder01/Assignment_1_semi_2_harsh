from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount


class ServiceChargeStrategy(ABC):
    """
    this is an asbtract base calss to define the service charge strategy for bank account
    """
    # this is the constant for the base service charge
    BASE_SERVICE_CHARGE = 10.00  


    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        this calculates the service charge based on the account balance.
        """
        pass