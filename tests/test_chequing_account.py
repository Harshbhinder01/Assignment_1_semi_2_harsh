import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
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
        self.assertEqual(round(self.chequing.get_service_charges(), 2), 10.0)


    def test_get_service_charges_less(self):    
        """
        this test balance less than overdraft limit
        """
        self.chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), -100.00, 0.05)
        charge = 0.50 + (-100.00- -300.00) * 0.5 
        self.assertEqual(round(self.chequing.get_service_charges(),2), 10.0)




    def test_get_service_charges_equal(self):
        """
        this is to test balance equal to overdraft limit
        """
        self.chequing = ChequingAccount(1020, 12, 50.00, date(2025, 2, 15), -100.00, 0.05)
        self.assertEqual(round(self.chequing.get_service_charges(),2), 10.0)



    def test_str_method(self):
        """
        this is to test appropriate value returned based on attribute values.
        """
        str_expected = (
            "Account Number: 1020 Balance: $50.0\n"
            "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing"

        )
        self.assertEqual(str(self.chequing), str_expected)

if __name__ == "__main__":
    unittest.main()
