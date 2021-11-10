class ClassElement:
    INDENT_BLOCK = " " * 2

    def __init__(self, name, type=None):
        self.name = name
        self.type = type
        self.elements = []

    def __str__(self):
        return self.__converter()

    def __converter(self):
        lines = []

        lines.append("class {}:".format(self.name))

        if len(self.elements) > 0:
            lines.append("{}def __init__(self):".format(ClassElement.INDENT_BLOCK))
            for idx in range(len(self.elements)):
                element = self.elements[idx]
                if element:
                    lines.append(
                        "{}self.{} = {}".format(ClassElement.INDENT_BLOCK * 2, element.type, element.name))
        else:
            lines.append("{}pass".format(ClassElement.INDENT_BLOCK))
        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.root = ClassElement(root_name)

    def add_field(self, type, name):
        self.root.elements.append(ClassElement(name, type))
        return self

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    p = CodeBuilder('Person').add_field('name', '""').add_field('age', '29')
    print(p)
    print(10 * "*")
    p = CodeBuilder('Foo')
    print(p)
    
