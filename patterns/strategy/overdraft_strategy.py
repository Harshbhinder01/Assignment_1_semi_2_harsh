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
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate
    
    @property
    def overdraft_limit(self) -> float:
        """
        this is the acessor for the overdraft limit
        """
        return self._overdraft_limit
    
    @property
    def overdraft_rate(self) -> float:
        """
        this is the acessor for the overdraft rate
        """
        return self._overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        this calculates the service charges based on the overdraft status of the account.
        if the balance of the chequing account is greater than or equal to the overdraft limit ,
        then the service charge is set to the base service charge value 
        if the balance of the chequing account is less than the overdraft limit, 
        then the service charge is calculated using the formula.
        """
        # this is the base service charge constant from the class service charge strategy

        if account.balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self._overdraft_limit - account.balance) * self._overdraft_rate