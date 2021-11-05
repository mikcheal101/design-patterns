class Person:
    def __init__(self) -> None:
        # address details
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income: float = 0.0

    def __str__(self) -> str:
        return f"Address: {self.street_address}, {self.postcode}, {self.city}" + \
            f"Employed at: {self.company_name} as a {self.postcode} earning {self.annual_income}"


class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person=person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income: float):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person=person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    person = pb\
        .lives\
        .at('123 London Road')\
        .in_city('Abuja')\
        .with_postcode()\
        .works\
        .at('Konga')\
        .as_a('Engineer')\
        .earning('$2,000.00')\
        .build()
