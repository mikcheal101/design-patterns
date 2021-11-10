class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw_point(self, point):
        print('.', end='')