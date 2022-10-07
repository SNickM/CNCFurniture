from unittest import TestCase, main
from src.module.wall import Wall

class StartPointTest(TestCase):
    def test_wall1(self):
        # проверка установки начальных координат
        self.wl = Wall(15, 15, 420, 480, 16)
        self.assertEqual(self.wl.x0, 15)
        self.assertEqual(self.wl.y0, 15)
        self.assertEqual(self.wl.z0, 0)

    def test_wall2(self):
        # проверка установки размеров стенки
        self.wl = Wall(15, 15, 420, 480, 16)
        self.assertEqual(self.wl.height, 420)
        self.assertEqual(self.wl._depth, 480)
        self.assertEqual(self.wl.thinckness, 16)

    def test_wall3(self):
        # проверка ручной установки размеров стенки
        self.wl = Wall(15, 15, 420, 480, 16)
        self.wl.height = 100
        self.wl.depth = 120

        self.assertEqual(self.wl.height, 100)
        self.assertEqual(self.wl._depth, 120)
        self.assertEqual(self.wl.thinckness, 16)


if __name__ == '__main__':
    main()
