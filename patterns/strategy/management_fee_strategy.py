__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    
    """
    def __init__(self, date_created: date, management_fee: float):
        """
        
        """

        