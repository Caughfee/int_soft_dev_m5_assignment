from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    A class that represents a savings account
    """
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
            self.__minimum_balance = float(minimum_balance)
        else:
            self.__minimum_balance = 50.00

        # New private attribute
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """
        Returns a string the savings account
        Returns:
            str: A string that shows account number, balance, minimum balance, and account type
        """
        string = super().__str__()
        string += (f"\nMinimum Balance: ${self.__minimum_balance:.2f}, Account Type: Savings")
        return string
    
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for a savings account
        Returns: float - The service charges
        """
        return self.__strategy.calculate_service_charges(self)