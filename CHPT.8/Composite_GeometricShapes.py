from abc import ABC


class GraphicObject(ABC):
    def __init__(self, color=None) -> None:
        super().__init__()
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def _print(self, items: list, depth: int = 0) -> None:
        # utility method print
        items.append('*' * depth)

        if self.color:
            items.append(self.color)
        items.append('{}\n'.format(self.name))

        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self) -> str:
        items = []
        self._print(items)
        return ' '.join(items)


class Circle(GraphicObject):
    @property
    def name(self) -> str:
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self) -> str:
        return 'Square'


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing.name = "My Drawing"
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))

    drawing.children.append(group)

    print(drawing)