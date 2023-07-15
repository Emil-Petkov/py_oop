from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class MultiFunction(Printable, Scannable, Faxable):
    def print(self, document):
        pass

    def scan(self):
        pass

    def fax(self, document):
        pass


class SimplePrinter(Printable):
    def print(self, document):
        pass
