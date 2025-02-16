from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    A class that represents an investment account
    """
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        """
        account_number (int): The account number
            client_number (int): The client number
            balance (float): The balance of the bank account
            date_created (date): The date it was created
            management_fee (float): The flat-rate fee the bank charges for managing an investment account
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(management_fee, (int, float)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55
        
