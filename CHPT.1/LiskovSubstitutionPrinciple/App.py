class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Width: {self.width}; Height: {self.height}"

    @property
    def area(self) -> float:
        return 1.0 * self._width * self._height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value) -> None:
        self._height = value

class Square(Rectangle):
    def __init__(self, side) -> None:
        Rectangle.__init__(self, side, side)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(shape):
    w = shape.width
    shape.height = 10
    expected = float(w * 10)

    print(f"Expected: {expected}, got: {shape.area}")

if __name__ == "__main__":
    rectangle = Rectangle(5, 8)
    use_it(rectangle)

    square = Square(5)
    use_it(square)
