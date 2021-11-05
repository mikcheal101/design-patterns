from typing import Sequence

INDENT_SIZE = 2


class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.__root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, name: str, text: str) -> None:
        self.__root._elements.append(
            HtmlElement(name, text)
        )

    def add_child_fluent(self, name: str, text: str):
        self.__root._elements.append(
            HtmlElement(name, text)
        )
        return self

    def __str__(self) -> str:
        return str(self.__root)


class HtmlElement:
    def __init__(self, name: str = '', text: str = '') -> None:
        self._text: str = text
        self._name: str = name
        self._elements: Sequence[HtmlElement] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __str(self, indentation):
        lines = []
        i = ' ' * (indentation * INDENT_SIZE)
        lines.append(f'{i}<{self.name}>')

        if self._text:
            x = ' ' * ((indentation + 1) * INDENT_SIZE)
            lines.append(f'{x}{self._text}')

        for element in self._elements:
            lines.append(element.__str(indentation + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name: str) -> HtmlBuilder:
        return HtmlBuilder(name)


if __name__ == "__main__":
    builder = HtmlElement.create('ul')
    builder.add_child('li', 'Hello')
    builder.add_child('li', 'World')
    builder.add_child('li', 'People')

    # builder.add_child_fluent('li', 'Green')\
    #     .add_child_fluent('li', 'Tea')\
    #     .add_child_fluent('li', 'Fleet')
    print('Ordinary Builder: ')
    print(builder)
