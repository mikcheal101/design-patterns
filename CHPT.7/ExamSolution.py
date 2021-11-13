# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

from abc import ABC


class Renderer(ABC):
    name = ""
    
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer

    def __str__(self):
        self.renderer.name = self.name
        return f'{self.renderer.what_to_render_as}'

class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return f'Drawing {self.name} as lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return f'Drawing {self.name} as pixels'


if __name__ == "__main__":
    raster = RasterRenderer()
    triangle = Triangle(renderer=raster)

    print(str(Triangle(VectorRenderer())))
    # print(str(Triangle(RasterRenderer())))
