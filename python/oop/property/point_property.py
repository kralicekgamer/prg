class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    @property
    def y(self):
        
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value
            

    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
p = Point(10, 20)
print(p)