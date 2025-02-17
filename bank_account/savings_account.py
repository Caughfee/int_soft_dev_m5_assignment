from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    A class that represents a savings account
    """
    SERVICE_CHARGE_PREMIUM = 2.0
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        """
        account_number (int): The account number
            client_number (int): The client number
            balance (float): The balance of the bank account
            date_created (date): The date it was created
            minimum_balance (float): the minimum value a balance can be before further service charges are applied
        """
        if isinstance(minimum_balance, (int, float)):
            self.__management_fee = float(minimum_balance)
        else:
            self.__management_fee = 50.00