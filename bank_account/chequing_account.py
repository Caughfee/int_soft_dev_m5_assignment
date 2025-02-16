from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    A class that represents a chequing account
    """
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the bank account information based on the values
        Args:
            account_number (int): The account number
            client_number (int): The client number
            balance (float): The balance of the bank account
            date_created (date): The date it was created
            overdraft_limit (float): the maximum amount a balance can be overdrawn before overdraft fees are applied
            overdraft_rate (float): the rate which overdraft fees will be applied
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(overdraft_limit, (int, float)):
            self.__overdraft_limit = float(overdraft_limit)
        else:
            self.__overdraft_limit = -100.00
        
        if isinstance(overdraft_rate, (int, float)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        """
        Returns a string representing the chequing account
        Returns:
            str: A string that shows account number, balance, overdraft limit and rate, and account type
        """
        string = super().__str__()
        string += (f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate*100:.2f}% Account Type: Chequing")
        return string
    
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for a chequing account
        Returns:
            float - The service charges
        """
        if self._BankAccount__balance >= self.__overdraft_limit:
            calculate_service_charge = self.BASE_SERVICE_CHARGE
            return calculate_service_charge
        else:
            calculate_service_charge = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self._BankAccount__balance) * self.__overdraft_rate
            return calculate_service_charge