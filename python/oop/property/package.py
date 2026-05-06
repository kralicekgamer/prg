class Package:
    def __init__(self, width, height, depth, weight):
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0 or value >= 20:
            exit()

        else:
            self._width = value



    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0 or value >= 20:
            exit()

        else:
            self._height = value




    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        if value < 0 or value >= 20:
            exit()

        else:
            self._depth = value



    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0 or value >= 50:
            exit()

        else:
            self._weight = value



p = Package(10, 15, 5, 20)
print("Width:", p.width)
print("Height:", p.height)
print("Depth:", p.depth)
print("Weight:", p.weight)

p.width = 12
p.height = 18
p.depth = 3
p.weight = 30

p.width = 25
print("pokud se vypise tohle je neco spatne")