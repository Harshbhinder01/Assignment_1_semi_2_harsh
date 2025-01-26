"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client


class testClient(unittest.TestCase):
    # attributes set to input values.
    def setUp(self):
      self.client = Client(100, "Harshdeep", "Bhinder", "Harshdeep.bhinder@gmail.com")

    #Exception raised when invalid client number.
    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            self.client = Client("abcd", "Harshdeep", "Bhinder", "Harshdeep.bhinder@gmail.com")