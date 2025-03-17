__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    A subclass of ServiceChargeStrategy that manages the Overdraft Strategy.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy based on the values.
        
        Args:
            overdraft_limit (float): the maximum amount a balance can be overdrawn before overdraft fees are applied
            overdraft_rate (float): the rate which overdraft fees will be applied
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Returns the calculated service charges for the bank account.
        Returns:
            float - The service charges
        """
        if account.balance >= self.__overdraft_limit:
            calculate_service_charge = self.BASE_SERVICE_CHARGE
            return calculate_service_charge
        else:
            calculate_service_charge = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance) * self.__overdraft_rate
            return calculate_service_charge