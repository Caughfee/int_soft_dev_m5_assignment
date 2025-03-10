__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    An abstract class that deals with the interface for service charges.
    Methods:
        calculate_service_charges: a method that will be implemented to subclasses of ServiceChargeStrategy
    """