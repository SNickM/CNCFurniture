####################################################################################
# Footing - крышка, дно, полка - горизонтальные части шириной width, глубиной depth и толщиной thinckness
####################################################################################
from src.module.shape import Shape
from src.module.point2d import Point2D

from src.module.compass3d import Compass3D


class Footing(Shape):

    def __init__(self, x0, y0, width, depth, thinckness):
        super().__init__(x0, y0, width, thinckness, depth)     # w x h x d
        self._thinckness = thinckness
        self.array_pt = []

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w


    @property
    def depth(self):
        return self._depth


    @depth.setter
    def depth(self, d):
        self._depth = d

    @property
    def thinckness(self):
        return self._thinckness

    # сформировать координаты отбражения вида "спереди" изделия
    def draw(self):
        self.array_pt = []
        self.array_pt.append(Point2D(self._x0, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0 + self._thinckness))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0 + self._thinckness))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0))

        return self.array_pt

    # сформировать координаты отбражения вида для ЧПУ (вид спереди для ЧПУ)
    def draw_cnc(self):
        self.array_pt = []
        self.array_pt.append(Point2D(self._x0, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0 + self._depth))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0 + self._depth))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0))

        return self.array_pt


if __name__ == '__main__':

    ft = Footing(10, 10, 420, 520, 16)
    print(ft.width, ft.depth, ft.thinckness)

    s = Compass3D()
    s.draw_object(ft.draw())
    ft.x0 = 10
    ft.y0 = 40
    s.draw_object(ft.draw_cnc())


