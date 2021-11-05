from enum import Enum
from typing import Sequence

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

class Relationships:
    def __init__(self) -> None:
        self.relations: Sequence[tuple[Person, int, Person]] = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def __str__(self) -> str:
        for index, relation in enumerate(self.relations):
            print(f"[{index}]: {relation[0].name} = {relation[1]} = {relation[2].name}")

class Research:
    def __init__(self, relationships: Relationships) -> None:
        for relation in relationships.relations:
            if relation[0].name == "John" and relation[1] == Relationship.PARENT:
                print(f"John has a child called {relation[2].name}")


if __name__ == "__main__":
    chris = Person("Chris")
    john = Person("John")
    robert = Person("Robert")
    gilbert = Person("Gilbert")
    matt = Person("Matt")

    relationships = Relationships()
    relationships.add_parent_and_child(chris, john)
    relationships.add_parent_and_child(chris, robert)
    relationships.add_parent_and_child(john, gilbert)
    relationships.add_parent_and_child(john, matt)

    research = Research(relationships)
