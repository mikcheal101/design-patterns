from abc import ABC


class Shape(ABC):
    def __str__(self) -> str:
        return ''


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def resize(self, factor: float) -> None:
        self.radius *= factor

    def __str__(self) -> str:
        return 'A circle of a radius: {}'.format(self.radius)


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def __str__(self) -> str:
        return 'A square with side: {}'.format(self.radius)


class ColoredShape(Shape):
    def __init__(self, shape: Shape, color: str) -> None:
        if isinstance(shape, ColoredShape):
            raise Exception('ColoredShape cannot be applied twice.')    
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return '{} has a color {}'.format(self.shape, self.color)


class TransparentShape(Shape):
    def __init__(self, shape: Shape, transparency: Shape) -> None:
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return "{} has {}% transparency".format(self.shape, self.transparency)

if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, 'red')
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 3)

    yellow_half_transparent_square = TransparentShape(ColoredShape(ColoredShape(Square(4), 'green'), 'yellow'), 3)
