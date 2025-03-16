from patterns.observer.observer import Observer

class Subject:
    """
    this is a class named Subject. it will maintain a list of its observers

    """

    def __init__(self) -> None:
        """
        this initlialized the class attribute to an empty list

        """
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """
        this will notify methods based on the information shwon in the class digram
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        this method declaed with the argument of name observer.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        this is the notify method
        """
        for observer in self._observers:
            observer.update(message)

