"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        """"""
        self.bankaccount = BankAccount(1234, 22, 25.00)
    
    def test_invalid_balance(self):
        """
        Balance attribute set to 0 when non-numeric balance argument.
        """
        self.bankaccount = BankAccount(1234, 22, 0.0)
        self.assertEqual(round(self.bankaccount.balance,2), 0.0)
    
    def test_account_number_invalid(self):
      """
      ValueError when non-numeric account number
      """
      with self.assertRaises(ValueError):
          self.bankaccount = BankAccount("harsh", 22, 25.00)
    
    def test_client_number_invalid(self):
        """
        ValueError when non-numeric client number
        """
        with self.assertRaises(ValueError):
            self.bankaccount = BankAccount(1234, "harsh", 25.00)
    
    def test_account_number(self):
        """
        returns account number attribute
        """
        self.assertEqual(self.bankaccount.account_number, 1234)
    
    def test_client_number(self):
        """
        returns client number attribute
        """
        self.assertEqual(self.bankaccount.client_number, 22)
    
    def test_balance(self):
        """
        returns balance attribute
        """
        self.assertEqual(round(self.bankaccount.balance,2), 25.00)
    
    def test_new_balance(self):
        """
        correctly updates balance attribute when positive amount is received.
        """
        self.bankaccount.deposit(10.00)
        self.assertEqual(round(self.bankaccount.balance, 2), 35.00)
    
    def test_new_negative_balance(self):
        """
        correctly updates balance attribute when negative amount is received.
        """
        with self.assertRaises(ValueError):
            self.bankaccount.deposit(-5.00)
    
    def test_non_numeric_balance(self):
        """
        Balance attribute value remains unchanged when amount is non-numeric
        """
        with self.assertRaises(ValueError):
            self.bankaccount.deposit("harsh")
    #
    def test_deposit_amount(self):
        """
        BankAccount object's balance is updated correctly when a valid amount is provided.
        """
        self.bankaccount.deposit(15.00)
        self.assertEqual(round(self.bankaccount.balance,2 ), 40.00)


    def test_not_positive_deposit(self):
        """
        ValueError when negative amount is provided.
        """
        with self.assertRaises(ValueError):
            self.bankaccount.deposit(-25.00)

    
    def test_valid_withdraw(self):
        """
        BankAccount object's balance is updated correctly when a valid amount is provided.
        """
        self.bankaccount.withdraw(5.00)
        self.assertEqual(round(self.bankaccount.balance, 2), 30.00)
    
    def test_invalid_withdraw_negative(self):
        """
        ValueError when negative amount is provided.
        """
        with self.assertRaises(ValueError):
            self.bankaccount.withdraw(-5.00)

   
    def test_withdraw_exceeds_balance(self):
        """
        ValueError when amount exceeds balance.
        """
        with self.assertRaises(ValueError):
            self.bankaccount.withdraw(100.00)
    
    
    def test_str_method(self):
        """
        returns string in expected format.
        """
        expected_str = "Account number: 1234 Balance: $25.0"
        self.assertEqual(str(self.bankaccount), expected_str)