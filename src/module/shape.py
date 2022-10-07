####################################################################################
# Shape - представление объекта в пространстве
####################################################################################
from src.module.startpoint import StartPoint


class Shape(StartPoint):  # 2Д форма: стенки, крышка, дно, полка
    # границы полей фрезерного станка
    MAX_X = 1000 - 20
    MAX_Y = 1500 - 20
    MAX_Z = 1000 - 20

    def __init__(self, x0, y0, width, height, depth):
        super().__init__(x0, y0)
        self._width = width         # ширина     используется либо ширина, либо глубина...
        self._depth = depth         # глубина
        self._height = height       # высота
        self.verify_size()
        # self._thinckness = thinckness

    @property
    def x_max(self):
        self.verify_size()
        return self._width + self.x0

    @property
    def y_max(self):
        return self._height + self.y0

    @property
    def z_max(self):
        return self._depth + self.z0

    def verify_size(self):
        if self._width + self.x0 > self.MAX_X:
            raise Exception("Размер по Х превышает допустимое значение...")

        if self._height + self.y0 > self.MAX_Y:
            raise Exception("Размер по Y превышает допустимое значение...")

        if self._depth + self.z0 > self.MAX_Z:
            raise Exception("Размер по Z превышает допустимое значение...")
        return True


if __name__ == '__main__':
    sh = Shape(10, 10, 420, 480, 520)
    print(sh.x_max, sh.y_max, sh.z_max)
    print(sh.verify_size())
