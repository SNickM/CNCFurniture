from unittest import TestCase, main
from src.module.shape import Shape

class ShapeTest(TestCase):
    def test_shape1(self):
        # проверка установки начала координат
        self.sh = Shape(15, 15, 420, 480, 520)
        self.assertEqual(self.sh.x0, 15)
        self.assertEqual(self.sh.y0, 15)
        self.assertEqual(self.sh.z0, 0)

    def test_shape2(self):
        # проверка возможности изменения начала координат
        self.sh = Shape(10, 10, 420, 480, 520)
        self.sh.x0 = 12
        self.sh.y0 = 22
        self.assertEqual(self.sh.x0, 12)
        self.assertEqual(self.sh.y0, 22)

    def test_shape3(self):
        # проверка вычисления границ объекта
        self.sh = Shape(10, 10, 420, 480, 520)
        self.assertEqual(self.sh.x_max, 430)
        self.assertEqual(self.sh.y_max, 490)
        self.assertEqual(self.sh.z_max, 520)

    def test_shape4(self):
        self.sh = Shape(10, 10, 420, 480, 520)
        self.assertEqual(self.sh.verify_size(), True)

        #self.sh1 = Shape(10, 10, 2420, 480, 520)
        #self.assertEqual(self.sh.verify_size(), True)

        #self.sh1 = Shape(10, 10, 420, 2480, 520)
        #self.assertEqual(self.sh.verify_size(), True)

        #self.sh1 = Shape(10, 10, 420, 480, 2520)
        #self.assertEqual(self.sh.verify_size(), True)

if __name__ == '__main__':
    main()
