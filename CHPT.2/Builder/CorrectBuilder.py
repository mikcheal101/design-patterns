class Person:
    def __init__(self) -> None:
        self.name: str = ""
        self.age: int = 0
        self.occupation: str = ""

    def __str__(self) -> str:
        return f'{self.name} is {self.age} and works as: {self.occupation}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name: str):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, value: str):
        self.person.occupation = value
        return self


class PersonAgeBuilder(PersonJobBuilder):
    def aged(self, value: int):
        self.person.age = value
        return self


if __name__ == "__main__":
    pb = PersonAgeBuilder()
    me = pb.called('Elvis').works_as_a('Quant').aged(23).build()
    print(me)
