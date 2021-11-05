from abc import abstractmethod

class IPrinter:
    @abstractmethod
    def printer(self, document):
        pass

class IScanner:
    @abstractmethod
    def scan(self, document):
        pass

class IFaxMachine:
    def fax(self, document):
        pass

class MyPrinter(Printer):
    def printer(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def printer(self, document):
        pass

    def scan(self, document):
        pass

class IMultiFunctionDevice(IPrinter, IScanner, IFaxMachine):
    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def printer(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class SubMultiDevice(IMultiFunctionDevice):
    def __init__(self, printer, scanner, fax_machine) -> None:
        super().__init__()
        self._fax_machine = fax_machine
        self._scanner = scanner
        self._printer = printer

    def fax(self, document):
        self._fax_machine.fax(document)
        print("Faxing....!")

    def printer(self, document):
        self._printer.print(document)
        print("Printing...!")

    def scan(self, document):
        self._scanner.scan(document)
        print("Scanning...!")
