__author__ = "Rogine Mirando"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    An abstract class that represents the Observer pattern
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Method to handle updates

        Args:
            message (str): The update message sent
        """
        pass