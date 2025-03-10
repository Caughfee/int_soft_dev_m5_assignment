__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    An abstract class that deals with the interface for service charges.
    Methods:
        calculate_service_charges: a method that will be implemented to subclasses of ServiceChargeStrategy.
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(account: BankAccount) -> float:
        """
        Deals wtih calculating the service charges for their respective strategy.

        Attributes:
            account (BankAccount): The bank account
        """
        pass