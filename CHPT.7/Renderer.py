from abc import ABC


class IRenderer(ABC):
    def render_circle(self, radius):
        pass
    # def render_square(self, radius):
    #    pass


class VectorRenderer(IRenderer):
    def render_circle(self, radius):
        print("Drawing a circle of radius {}".format(radius))


class RasterRenderer(IRenderer):
    def render_circle(self, radius):
        print("Drawing pixels for a circle of radius {}".format(radius))


class Shape(ABC):
    def __init__(self, renderer: IRenderer) -> None:
        self.renderer = renderer

    def draw(self):
        """ Base class """
        pass

    def resize(self, factor: float):
        """ Base class """
        pass


class Circle(Shape):
    def __init__(self, renderer: IRenderer, radius: int) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
