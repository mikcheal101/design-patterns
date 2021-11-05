from abc import abstractmethod
from enum import Enum
from typing import Generator, Sequence

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

class IRelationship:
    @abstractmethod
    def find_children_by_parent_name(self, name):
        pass

class Relationships(IRelationship):
    def __init__(self) -> None:
        self.relations: Sequence[tuple[Person, int, Person]] = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_children_by_parent_name(self, name: str) -> Generator[Person, None, None]:
        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.PARENT:
                yield relation[2]

    def __str__(self) -> str:
        for index, relation in enumerate(self.relations):
            print(f"[{index}]: {relation[0].name} = {relation[1]} = {relation[2].name}")

class Research:
    def __init__(self, relationships: Relationships) -> None:
        name = "John"
        for relation in relationships.find_children_by_parent_name(name):
            print(f"{name} has a child called {relation.name}")


if __name__ == "__main__":
    chris = Person("Chris")
    john = Person("John")
    robert = Person("Robert")
    gilbert = Person("Gilbert")
    matt = Person("Matt")

    print("we are here")

    relationships = Relationships()
    relationships.add_parent_and_child(chris, john)
    relationships.add_parent_and_child(chris, robert)
    relationships.add_parent_and_child(john, gilbert)
    relationships.add_parent_and_child(john, matt)

    research = Research(relationships)
