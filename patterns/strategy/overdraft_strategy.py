from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    this is the overDraftStratery class

        overdraft_limit (float): The maximum amount the balance can be overdrawn.
        overdraft_rate (float): The rate at which overdraft fees will be applied.
    """


    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        this is to initialize the object overdraft strategy.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        this calculates the service charges based on the overdraft status of the account.
        if the balance of the chequing account is greater than or equal to the overdraft limit ,
        then the service charge is set to the base service charge value 
        if the balance of the chequing account is less than the overdraft limit, 
        then the service charge is calculated using the formula.
        """
        # this is the base service charge  from the class service charge strategy
        base_service_charge = self.BASE_SERVICE_CHARGE

        if account.balance >= self.__overdraft_limit:
            return base_service_charge
        else:
            # Calculate charge based on overdraft
            return (base_service_charge + (self.__overdraft_limit - account.balance) * self.__overdraft_rate)