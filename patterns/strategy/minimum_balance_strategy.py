__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    
    """
    def __init__(self, minimum_balance: float):
        """
        
        """
        