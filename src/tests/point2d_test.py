from unittest import TestCase, main
from src.module.point2d import Point2D


class Point2DTest(TestCase):
    def test_point2d1(self):
        # создание объекта без аргументов
        self.pt = Point2D()
        self.assertEqual(self.pt.x, 0)
        self.assertEqual(self.pt.y, 0)

    def test_point2d2(self):
        # создание объекта с аргументами
        self.pt = Point2D(15, 150)
        self.assertEqual(self.pt.x, 15)
        self.assertEqual(self.pt.y, 150)

    def test_point2d3(self):
        # проверка возможности присвоения значений
        self.pt = Point2D()
        self.pt.x = 20
        self.pt.y = 11
        self.assertEqual(self.pt.x, 20)
        self.assertEqual(self.pt.y, 11)


if __name__ == '__main__':
    main()
