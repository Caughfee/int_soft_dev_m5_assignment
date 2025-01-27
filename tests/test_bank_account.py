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
        # Set up runs automatically before each test method and gives inital values
        self.bank_account = BankAccount(1, 2, 310.00)

    def test_init_valid(self):
        # Arrange & Act
        bank_account = BankAccount(1, 2, 310.00)

        # Assert
        self.assertEqual(bank_account.account_number, 1)
        self.assertEqual(bank_account.client_number, 2)
        self.assertEqual(bank_account.balance, 310.00)
    
    def test_balance_invalid(self):
        # arrange & act
        bank_account = BankAccount(1, 2, "asdw")

        # assert
        self.assertEqual(bank_account.balance, 0)
    
    def test_invalid_account_number(self):
        # Arrange & assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("yes", 2, 310.00)
    
    def test_invalid_client_number(self):
        # Arrange & assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(1, "hyes", 310.00)
    
    def test_account_number(self):
        # Set up done above

        # Assert
        self.assertEqual(self.bank_account.account_number, 1)

    def test_client_number(self):
        # Set up done above

        # Assert
        self.assertEqual(self.bank_account.client_number, 2)

    def test_balance(self):
        # Set up done above

        # Assert
        self.assertEqual(self.bank_account.balance, 310.00)

    def test_update_balance_positive(self):
        # Arrange and act
        self.bank_account.update_balance(100.00)

        # Assert
        self.assertEqual(self.bank_account.balance, 410.00)
    
    def test_update_balance_negative(self):
        # Arrange and act
        self.bank_account.update_balance(-100.00)

        # Assert
        self.assertEqual(self.bank_account.balance, 210.00)

    def test_deposit(self):
        # Arrange and act
        self.bank_account.deposit(100.00)

        # Assert
        self.assertEqual(self.bank_account.balance, 410.00)

    def test_deposit_negative(self):
        # Arrange Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100.00)

    def test_withdraw(self):
        # Arrange and act
        self.bank_account.withdraw(100.00)

        # Assert
        self.assertEqual(self.bank_account.balance, 210.00)

    def test_withdraw_negative(self):
        # Arrange and assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100.00)

    def test_withdraw_exceed(self):
        # Arrange and assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(400.00)

    def test_str_(self):
        # Arrange and act
        expected = ("Account Number: 1 Balance: $310.00")

        # Assert
        self.assertEqual(expected, str(self.bank_account))