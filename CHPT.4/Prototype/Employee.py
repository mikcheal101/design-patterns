import copy


class Address:
    def __init__(self, street_address: str, suite: str, city: str) -> None:
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self) -> str:
        return "{}, Suite #: {}, {}.".format(self.street_address, self.suite, self.city)


class Employee:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return "{} works at {}".format(self.name, self.address)


class EmployeeFactory:
    main_office_employee = Employee('', address=Address(
        city="London", street_address="123 Lekki Dr.", suite=0))
    aux_office_employee = Employee('', address=Address(
        city="Lagos", street_address="3B Herbert Mac. Way", suite=0))

    @staticmethod
    def __new_employee(prototype: Employee, name: str, suite: int) -> Employee:
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_aux_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)


if __name__ == "__main__":
    john = EmployeeFactory.new_main_office_employee("John", 101)
    jane = EmployeeFactory.new_main_office_employee("Jane", 103)
    philip = EmployeeFactory.new_main_office_employee("Philip", 300)
    sandra = EmployeeFactory.new_aux_office_employee("Sandra", 1)

    for i in [john, jane, philip, sandra]:
        print(i)
