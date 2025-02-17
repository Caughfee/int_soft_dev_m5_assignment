import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def test_init(self):
        # Arrange
        account = SavingsAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0)

        # Act and Assert
        self.assertEqual(account.account_number, 123)
        self.assertEqual(account.client_number, 456)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account._date_created, date(2022, 1, 1))
        self.assertEqual(account._SavingsAccount__minimum_balance, 500.0)

    def test_init_invalid_minimum_balance(self):
        # Arrange
        account = SavingsAccount(123, 456, 1000.0, date(2022, 1, 1), "bacon")

        # Act and Assert
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.00)

    def test_service_charges_above_minimum_balance(self):
        # Arrange
        account = SavingsAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50)

    def test_get_service_charges_equal_minimum_balance(self):
        # Arrange
        account = SavingsAccount(123, 456, 500.0, date(2022, 1, 1), 500.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50)

    def test_get_service_charges_below_minimum_balance(self):
        # Arrange
        account = SavingsAccount(123, 456, 400.0, date(2022, 1, 1), 500.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50 * 2.0)

    def test_str(self):
        # Arrange
        account = SavingsAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0)

        # Act and Assert
        account_str = str(account)
        expected_result = ("Account Number: 123 Balance: $1000.00\n"
                           "Minimum Balance: $500.00, Account Type: Savings")
        self.assertEqual(account_str, expected_result)