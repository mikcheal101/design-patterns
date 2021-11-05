from enum import Enum
import math


class CoordinateSystem(Enum):
    POLAR = 0
    CARTESIAN = 1


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * math.cos(b)
            self.y = a * math.sin(b)
