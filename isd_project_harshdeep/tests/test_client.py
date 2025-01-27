"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

from client.client import Client   
import unittest

class TestClient(unittest.TestCase):
    def setUp(self):
        """"""
        self.client = Client (100, "harsh", "bhinder", "harshbhinder@pixel.com")
    
    def test_client_num(self):
        """
        this test if the client number is not a int
        """
        with self.assertRaises(ValueError):
            self.client = Client ("harsh", "harsh", "bhinder", "harshbhinder@pixel.com")
    
    def test_first_name_invalid(self):
        """
        this test if the first name is invalid
        """
        with self.assertRaises(ValueError):
            self.client = Client (100, "", "bhinder", "harshbhinder@pixel.com")
    
    def test_last_name_invalid(self):
        """
        this is to test if the last name is invalid
        """
        with self.assertRaises(ValueError):
            self.client = Client (100, "harsh", "", "harshbhinder@pixel.com")
    
    def test_email_address_invalid(self):
        """
        this test if the email address is invalid"""
        with self.assertRaises(ValueError):
            self.client = Client (100, "harsh", "bhinder", "harshdeepbhinder@pixel.com")

    


    




if __name__ == "__main__":
    unittest.main()