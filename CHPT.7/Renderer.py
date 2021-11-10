from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass
    # def render_square(self, radius):
    #    pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing a circle of radius {}".format(radius))


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing a circle of radius {}".format(radius))
