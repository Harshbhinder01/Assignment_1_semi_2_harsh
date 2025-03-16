from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    this is a calss that represents the minimum balance strategy for bank accounts.
    """

    def __init__(self, minimum_balance: float):
        """
        Initialize the MinimumBalanceStrategy object.

        Args:
            minimum_balance (float): The minimum balance to be maintained in the account.
        """
        self.__minimum_balance = minimum_balance
        self.SERVICE_CHARGE_PREMIUM: float = 2.0

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges based on the account's balance.

        if balance of the savings account is greater or equal to the minimum balance,
        then the service is set to the base service charge value.
        if the balance of the savings account is less than the minimum balance,
        then the service charge is calculated using using the formula.

        """
        if account.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM 