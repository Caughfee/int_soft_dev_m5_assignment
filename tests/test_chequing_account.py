import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    def test_init(self):
        # Arrange
        account = ChequingAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0, 0.05)

        #Act and assert
        self.assertEqual(account.account_number, 123)
        self.assertEqual(account.client_number, 456)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account._date_created, date(2022, 1, 1))
        self.assertEqual(account._ChequingAccount__overdraft_limit, 500.00)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_overdraft_limit_invalid(self):
        # arrange
        account = ChequingAccount(123, 456, 1000.0, date(2022, 1, 1), "bacon", 0.05)

        # act and assert
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.00)

    def test_overdraft_rate_invalid(self):
        # arrange
        account = ChequingAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0, "bacon")

        # act and assert
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_invalid_date(self):
        # Arrange
        account_number = 123
        client_number = 456
        balance = 1000.0
        date_created = "bacon"
        overdraft_limit = 500.0
        overdraft_rate = 0.05

        # act and assert
        with self.assertRaises(ValueError):
            account = ChequingAccount(account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate)

    def test_balance_greater_than_limit(self):
        # Arrange 
        account = ChequingAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0, 0.05)

        # Act and Arrange
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50)

    def test_balance_less_than_limit(self):
        # Arrange
        account = ChequingAccount(123, 456, 400.0, date(2022, 1, 1), 500.0, 0.05)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(round(service_charges, 2), round(0.50 + (500.0 - 400.0) * 0.05, 2))

    def test_balance_equal_to_limit(self):
        # Arrange 
        account = ChequingAccount(123, 456, 500.0, date(2022, 1, 1), 500.0, 0.05)

        # Act and Arrange
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50)

    def test_str(self):
        account = ChequingAccount(123, 456, 1000.0, date(2022, 1, 1), 500.0, 0.05)

        # Act and Assert
        account_str = str(account)
        expected_result = ("Account Number: 123 Balance: $1000.00\n"
                           "Overdraft Limit: $500.00 Overdraft Rate: 5.00% Account Type: Chequing")
        self.assertEqual(account_str, expected_result)