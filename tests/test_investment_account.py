import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def test_init(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2022, 1, 1), 50.0)

        # Act and Assert
        self.assertEqual(account.account_number, 123)
        self.assertEqual(account.client_number, 456)
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(account._date_created, date(2022, 1, 1))
        self.assertEqual(account._InvestmentAccount__management_fee, 50.0)

    def test_invalid_management_fee(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2022, 1, 1), "bacon")

        # Act and Assert
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_service_charges_more_ten_years(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2010, 1, 1), 50.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 0.50)

    def test_get_service_charges_exactly_ten_years(self):
        # Arrange
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        account = InvestmentAccount(123, 456, 1000.0, ten_years_ago, 50.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 50.50)

    def test_get_service_charges_within_ten_years(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2022, 1, 1), 50.0)

        # Act and Assert
        service_charges = account.get_service_charges()
        self.assertEqual(service_charges, 50.50)

    def test_str_more_than_ten_years(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2010, 1, 1), 50.0)

        # Act and Assert
        account_str = str(account)
        expected_result = ("Account Number: 123 Balance: $1000.00\n"
                           "Management Fee: Waived Account Type: Investment")
        self.assertEqual(account_str, expected_result)

    def test_str_within_ten_years(self):
        # Arrange
        account = InvestmentAccount(123, 456, 1000.0, date(2022, 1, 1), 50.0)

        # Act and Assert
        account_str = str(account)
        expected_result = ("Account Number: 123 Balance: $1000.00\n"
                           "Management Fee: $50.00 Account Type: Investment")
        self.assertEqual(account_str, expected_result)
