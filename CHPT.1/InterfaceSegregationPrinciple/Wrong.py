
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        # do nothing
        pass

    def scan(self, document):
        """ Not Supported! """
        raise NotImplementedError("Printer cannot scan!")

