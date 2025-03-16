import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta
from patterns.strategy.managment_fee_strategy import ManagementFeeStrategy

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """
        attributes are set to input values
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2025, 2, 15), 2.00)


    def test_managment_invalid_type(self):
        """
        this is to test the managment fee when it has a invalid type.
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2025, 2, 15),"harshdeep")
        self.assertEqual(round(self.investment._InvestmentAccount__managment_fee, 2), 2.55)




    def test_get_service_charges_more_than(self):
        """
        this is to test if the date was created more than 10 years ago
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2010, 2, 15), 2.00)
        expected_charge = ManagementFeeStrategy(date(2010, 2, 15), 2.00) .calculate_service_charges(self.investment)
        self.assertEqual(expected_charge, self.investment.get_service_charges())

    def test_get_service_charges_exactly(self):
        """
        this is to test if the date was created exactly 10 years ago
        
        """
        years = date.today() - timedelta(days=10 * 365.25)
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2015, 2, 15), 2.00)
        self.assertEqual(round(self.investment.get_service_charges(), 2), 10)

    def test_get_service_charges_within(self):
        """
        this is to test if the date was created within the last 10 years
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2023, 2, 15), 2.00)
        self.assertEqual(round(self.investment.get_service_charges(), 2), 12.0)


    def test_str_waived(self):
        """
        this is to test if the init displays the waived managment fee when the date was created more than
        10 years ago
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2025, 2, 15), 2.00)
        expected = (f"Account Number: 1020 Balance: $50.0\n"
                            f"Management Fee: $2.00 Account Type: Investment"
        )
        self.assertEqual(str(self.investment), expected)


    def test_str_date_created_within_ten_years(self):
        """
        displays managment fee when date created was within last 10 years
        """
        self.investment = InvestmentAccount(1020, 12, 50.00, date(2025, 2, 15), 2.00)
        expected = (f"Account Number: 1020 Balance: $50.0\n"
            f"Management Fee: $2.00 Account Type: Investment")
        self.assertEqual(str(self.investment), expected)





    

