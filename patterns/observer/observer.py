from abc import ABC, abstractmethod

class Observer(ABC):
    """
    this is a class named observer.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        it will be used to the interface.
        """
        pass
