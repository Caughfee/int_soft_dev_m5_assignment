from patterns.observer.observer import Observer

class Subject:
    """
    A class that represents the Subject in the observer pattern
    """

    def __init__(self):
        """
        Initializes the Subject class
        """
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """
        Attaches an observer
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detaches an observer
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notifies all observers with a message
        """
        for observer in self._observers:
            observer.update(message)