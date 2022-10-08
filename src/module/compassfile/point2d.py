####################################################################################
# Point2D - класс координат точки на плоскости
####################################################################################

class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # геттер для x0
    @property
    def x(self):
        return self._x

    # сеттер для x0
    @x.setter
    def x(self, x):
        self._x = x

    # геттер для y0
    @property
    def y(self):
        return self._y

    # сеттер для y0
    @y.setter
    def y(self, y):
        self._y = y


if __name__ == '__main__':
    pt2d = Point2D(10, 10)
    print(pt2d.__dict__)
    print(pt2d.x, pt2d.y)

    pt2d.x = 20
    pt2d.y = 30
    print(pt2d.x, pt2d.y)