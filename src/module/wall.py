####################################################################################
# Wall - боковая стенка глубиной depth, высотой height и тощиной thinckness
####################################################################################
from shape import Shape

class Wall(Shape):    # боковая стенка

    def __init__(self, x0, y0, height, depth, thinckness):
        super().__init__(x0, y0, thinckness, height, depth)     # w x h x d
        self._thinckness = thinckness

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


if __name__ == '__main__':

    wl = Wall(10,10, 480, 520, 16)
    print(wl.height, wl.depth, wl.thinckness)
    print(wl.__dict__)
