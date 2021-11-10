import copy

class Address:
    def __init__(self, street_address: str, city: str, country: str) -> None:
        self.street_address = street_address
        self.city = city
        self.county = country

    def __str__(self) -> str:
        return "{}, {}, {}.".format(self.street_address, self.city, self.county)


class Person:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return "{} lives at {}".format(self.name, self.address)


if __name__ == "__main__":
    address = Address("123 road", "London", "UK")
    john = Person("John", address)
    philip = copy.deepcopy(john)
    philip.name = "Philip"
    philip.address = "Mongomery road yaba"

    print(john)
    print(10 * "*")
    jane = john
    jane.name = "Jane"
    print(john)
    print(jane)
    print(philip)

