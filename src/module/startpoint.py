####################################################################################
# Класс StartPoint - начальная точка отображения объекта
####################################################################################
class StartPoint:

    def __init__(self, x0=10, y0=10): # конструктор
        self._x0 = x0   # левый нижний угол
        self._y0 = y0   # левый нижний угол
        self._z0 = 0    # для будущего использования

    # геттер для x0
    @property
    def x0(self):
        return self._x0

    # сеттер для x0
    @x0.setter
    def x0(self, x0):
        self._x0 = x0

    # геттер для y0
    @property
    def y0(self):
        return self._y0

    # сеттер для y0
    @y0.setter
    def y0(self, y0):
        self._y0 = y0

    # геттер для z0
    @property
    def z0(self):
        return self._z0

    # сеттер для z0
    #@z0.setter
    #def z0(self, z0):
    #    self._z0 = z0

    # отображение на чертеже общего вида
    def draw(self):
        pass

    # отображение на чертеже для ЧПУ
    def draw_cnc(self):
        pass


if __name__ == '__main__':
    pt = StartPoint(1, 1)
    print(pt.x0, pt.y0, pt.z0)
    pt.x0 = 5
    pt.y0 = 2
    #pt.z0 = 1   # сеттер не определен
    print(pt.x0, pt.y0, pt.z0)
    print(pt.__dict__)

    pt1 = StartPoint()
    print(pt1.x0, pt1.y0, pt1.z0)

