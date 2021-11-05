class Person:
    def __init__(self) -> None:
        self.name = ""
        self.age = 0

class CodeBuilder:
    def __init__(self, root_name: str) -> None:
        self.person = Person()
        self.person.name = root_name

    def add_field(self, type: str, value):
        if (type == 'name'):
            self.person.name = value
        elif (type == 'age'):
            self.person.age = value

    def __str__(self) -> str:
        pass

if __name__ == "__main__":
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', 0)
    print(cb)