import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        """
        this sets the attributes to the values
        """
        self.saving = SavingsAccount(1020, 12, 100.00, date(2025, 2, 15), 50.00)

    
    def test_invalid_minimum_balance(self):
        """
        this test if the minimum balance has a invalid type 
        """
        self.saving = SavingsAccount(1020, 12, 100.00, date(2025, 2, 15), "harsh")
        self.assertEqual(self.saving.minimum_balance, 50.00)


    def test_get_service_charges_greater(self):
        """
        this test the balance is greater than the minimum balance
        """
        self.saving = SavingsAccount(1020, 12, 100.00, date(2025, 2, 15), 50.00)
        self.assertEqual(self.saving.get_service_charges(),self.saving.BASE_SERVICE_CHARGE)

    def test_get_service_charges_equal(self):
        """
        this test the balance to see if it is equal to the minimum balance
        """
        self.saving = SavingsAccount(1020, 12, 50.00, date(2025, 2, 15), 50.00)
        self.assertEqual(self.saving.get_service_charges(), self.saving.BASE_SERVICE_CHARGE)

    def test_get_service_charges_less(self):
        """
        this test the balance to see if it is less to the minimum balance
        """
        self.saving = SavingsAccount(1020, 12, 10.00, date(2025, 2, 15), 50.00)
        self.assertEqual(round(self.saving.get_service_charges(),2),round(self.saving.BASE_SERVICE_CHARGE * self.saving.SERVICE_CHARGE_PREMIUM, 2))

    def test_str(self):
        """
        test to see if the displayed str
        """
        expected = (
            f"Account Number: 1020 Balance: $100.0\n"
             "Minimum Balance: $50.00 Account Type: Savings"

        )
        self.assertEqual(str(self.saving), expected) 

