from enum import Enum
import math


class CoordinateSystem(Enum):
    POLAR = 0
    CARTESIAN = 1


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    polar = Point.new_polar_point(1, 2)
    print(p, polar)
