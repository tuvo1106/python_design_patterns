"""
Interface Segregation Principle
- Don't put too much into an interface
- Split into separate interfaces
- YAGNI - You Aint Gonna Need It
"""

#before

class Machine:
    def print(self, doc):
        raise NotImplementedError

    def fax(self, doc):
        raise NotImplementedError

    def scan(self, doc):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, doc):
        pass

    def fax(self, doc):
        pass

    def scan(self, doc):
        pass

class OldFashionedPrinter(Machine):
    def print(self, doc):
        # ok
        pass

    def fax(self, doc):
        # cannot fax
        pass

    def scan(self, doc):
        # cannot scan
        pass

#after

from abc import abstractmethod

class Printer:
    @abstractmethod
    def print(self, doc):
        pass

class Scanner:
    @abstractmethod
    def scan(self, doc):
        pass

class MyPrint(Printer):
    def print(self, doc):
        print(doc)

class Photocopier(Printer, Scanner):
    def print(self, doc):
        pass

    def scan(self, doc):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, doc):
        pass

    @abstractmethod
    def scan(self, doc):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, doc):
        self.printer.print(doc)

    def scan(self, doc):
        self.scanner.scan(doc)
