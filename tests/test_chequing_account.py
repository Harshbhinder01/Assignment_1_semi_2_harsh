from bank_account.chequing_account import ChequingAccount
import unittest
from datetime import date

class testchequingaccount(unittest.Testcase):
    def setUp(self):
        """
        attributes are set to input values
        """
        self.chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), -100.00, 0.05)

    def test_invalid_overdraft_limit(self):
        """
        this test the overdraft limit by giving it a invalid input
        """
        
        self.chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), "harsh", 0.05)
    
    def test_invalid_overdraft_rate(self):
        """
        this test the overdraft rate by giving it a invalid input
        """
        self.chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), -100.00, "harsh")

    def test_invalid_date(self):
        """
        this is to test invalid date by giving it a invalid input
        """
        self.chequing = self.chequing = ChequingAccount(1020, 12, 50.00, "harsh", -100.00, 0.05)

    def test_get_service_charges_greater(self):
        """
        this test when balance is greater than overdraft limit
        """


    def test_get_service_charges_less(self):
        """
        this test balance less than overdraft limit
        """


    def test_get_service_charges_equal(self):
        """
        this is to test balance equal to overdraft limit
        """


    def test_str_method(self):
        """
        this is to test appropriate value returned based on attribute values.
        """
