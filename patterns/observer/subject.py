from patterns.observer.observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    A class that represents the Subject in the observer pattern
    """

    def __init__(self):
        """
        Initializes the Subject class
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attaches an observer
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detaches an observer
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Notifies all observers with a message
        """
        pass