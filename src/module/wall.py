####################################################################################
# Wall - боковая стенка глубиной depth, высотой height и тощиной thinckness
####################################################################################
from src.module.shape import Shape
from src.module.point2d import Point2D

from src.module.compass3d import Compass3D



class Wall(Shape):    # боковая стенка
    def __init__(self, x0, y0, height, depth, thinckness):
        super().__init__(x0, y0, thinckness, height, depth)     # w x h x d
        self._thinckness = thinckness

        self.array_pt = []


    @property
    def height(self):
        return self._height
#        return super()._height

    @height.setter
    def height(self, h):
        self._height = h


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
        self.array_pt.append(Point2D(self._x0, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._thinckness, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._thinckness, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0))

        return self.array_pt



    # сформировать координаты отбражения вида для ЧПУ (вид спереди для ЧПУ)
    def draw_cnc(self):
        self.array_pt = []
        self.array_pt.append(Point2D(self._x0, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._depth, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._depth, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0))

        return self.array_pt


if __name__ == '__main__':

    wl = Wall(10, 10, 480, 520, 16)
    print(wl.height, wl.depth, wl.thinckness)

    s = Compass3D()
    s.draw_object(wl.draw())
    wl.x0 = 40
    wl.y0 = 10
    s.draw_object(wl.draw_cnc())



