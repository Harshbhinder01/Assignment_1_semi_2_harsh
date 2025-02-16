from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):

        super().__init__(account_number, client_number, balance, date_created)
    
        try:
            self.__managment_fee = float(management_fee)
        except ValueError:
            self.__managment_fee = 2.55

    @property
    def managment_fee(self) -> float:
        """
        this returns the managment fee
        """
        return self.__managment_fee
    
    
    def get_service_charges(self) -> float:
        """
        if the date created is more than 10 years ago, the service charge is equal to the base service charge.
        otherwise the service charge is equal to the base service charge + managment fee.
        """
        if self.__date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self.__managment_fee
    
    def __str__(self) -> str:
        """
        if the account is more than 10 years old the managment fee is waived
        """
        if self.date_created < self.TEN_YEARS_AGO:
            management_fee_str = "Waived"
        else:
            management_fee_str = f"${self.__managment_fee,:.2f}"

        return (super().__str__() +
                f"Management Fee: {management_fee_str}\n" +
                "Account Type: Investment")

    