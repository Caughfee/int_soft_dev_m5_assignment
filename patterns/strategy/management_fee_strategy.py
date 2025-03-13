__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A subclass of ServiceChargeStrategy that manages service fees based on account creation date
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy based on the values
        Args:
            date_created (date): The creation date of the account
            management_fee (float): The annual management fee for the account
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount):
        """
        Calculates the service charges for the bank account
        Returns:
            float: The service charges
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
            return calculated_service_charge
        else:
            calculated_service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee
            return calculated_service_charge

