__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A subclass of ServiceChargeStrategy that calculates service charges based on the minimum balance
    """
    SERVICE_CHARGE_PREMIUM = 2.0
    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy
        Args:
            minimum_balance (float): The minimum balance required before getting charged the premium
        """
        self.__minimum_balance = minimum_balance
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges for the bank account
        Returns:
            float: The service charges
        """
        if account.balance >= self.__minimum_balance:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
            return calculated_service_charge
        else:
            calculated_service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
            return calculated_service_charge