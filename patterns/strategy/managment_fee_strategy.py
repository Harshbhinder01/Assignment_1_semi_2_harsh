from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    this is a class to represent the managment fee strategy for the investment account
    """

    # Define the constant for 10 years ago at the class level
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        this initialize the management fee strategy object.
        """
        self.__management_fee = management_fee
        self.__date_created = date_created 


    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        If the account is older than 10 years the managment fee gets wavied
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee 
