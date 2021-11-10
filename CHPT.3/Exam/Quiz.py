class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class PersonFactory:
    counter = 0
    def create_person(self, name) -> Person:
        PersonFactory.counter += 1
        return Person(PersonFactory.counter, name)

        

if __name__ == "__main__":
    for i in ['James', 'Philip', 'Matthew']:
        p = PersonFactory().create_person(i)
        print(p)

