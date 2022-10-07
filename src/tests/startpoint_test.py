from unittest import TestCase, main
from src.module.startpoint import StartPoint

class StartPointTest(TestCase):
    def test_startpoint1(self):
        # создание объекта без аргументов
        self.sp = StartPoint()
        self.assertEqual(self.sp.x0, 10)
        self.assertEqual(self.sp.y0, 10)
        self.assertEqual(self.sp.z0, 0)

    def test_startpoint2(self):
        # создание объекта с аргументами
        self.sp = StartPoint(15, 150)
        self.assertEqual(self.sp.x0, 15)
        self.assertEqual(self.sp.y0, 150)
        self.assertEqual(self.sp.z0, 0)

    def test_startpoint3(self):
        # проверка возможности присвоения значений
        self.sp = StartPoint()
        self.sp.x0 = 20
        self.sp.y0 = 11
        self.assertEqual(self.sp.x0, 20)
        self.assertEqual(self.sp.y0, 11)
        self.assertEqual(self.sp.z0, 0)


if __name__ == '__main__':
    main()

