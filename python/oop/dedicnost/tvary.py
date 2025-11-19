class Polygon:
    def __init__(self, sides):
        self.__sides = sides # __ privátní


    """
    Getter
    """
    def getSides(self):
        return self.__sides


    """
    Setter
    """
    def setSides(self, sides):
        self.__sides = sides

    """
    Když vytiskneme třídu
    """
    def __str__(self):
        return "Počet stran: " + str(self.getSides())


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def __str__(self):
        return "Počet stran: " + str(self.getSides()) + " dycky trujuhelnik"


class Pentagon(Polygon):
    def __init__(self):
        super().__init__(5)

    def __str__(self):
        return "Počet stran: " + str(self.getSides()) + " dycky pentagon"

p = Polygon(5)
# print(p.__sides) - nejde err
print(p.getSides())
print(p)


t = Triangle()
print(t)

pe = Pentagon()
print(pe)