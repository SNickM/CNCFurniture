####################################################################################
# Front - передняя стенка, задняя стенка, фасад шириной width, высотой height и толщиной thinckness
####################################################################################
from src.module.shape import Shape
from src.module.point2d import Point2D

from src.module.compass3d import Compass3D


class Front(Shape):   # передняя стенка

    def __init__(self, x0, y0, width, height, thinckness):
        super().__init__(x0, y0, width, height, thinckness)     # w x h x d
        self._thinckness = thinckness

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w


    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, d):
        self._height = d

    @property
    def thinckness(self):
        return self._thinckness

    # сформировать координаты отбражения вида "спереди" изделия
    def draw(self):
        self.array_pt = []
        self.array_pt.append(Point2D(self._x0, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0 + self._height))
        self.array_pt.append(Point2D(self._x0 + self._width, self._y0))
        self.array_pt.append(Point2D(self._x0, self._y0))

        return self.array_pt

    # сформировать координаты отбражения вида для ЧПУ (вид спереди для ЧПУ)
    def draw_cnc(self):
        return self.draw()


if __name__ == '__main__':

    fr = Front(10, 10, 420, 480, 16)
    print(fr.width, fr.width, fr.thinckness)

    s = Compass3D()
    s.draw_object(fr.draw())
    fr.x0 = 440
    fr.y0 = 10
    s.draw_object(fr.draw_cnc())
