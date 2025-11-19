class Animal:
    def __init__(self, name, sound, weight):
        self.__name = name
        self.__sound = sound
        self.__weight = weight

    def getName(self):
        return self.__name

    def getSound(self):
        return self.__sound

    def __str__(self):
        return "Moje jméno je: " + str(self.getName())


class Dog(Animal):
    def __init__(self, name, sound, weight, kind):
        super().__init__(name, sound, weight)  
        self.__kind = kind

    def stekej(self):
        print(str(Animal.getSound(self)))


class Cat(Animal):
    def __init__(self, name, sound, weight, color):
        super().__init__(name, sound, weight)  
        self.__color = color

    def mnoukej(self):
        print(str(Animal.getSound(self)))



d = Dog("Michal", "WOF!", 20, "Československý ovčák")
c = Cat("Adéla", "MIAU!", 8, "Černá")

print(d)
print(c)

d.stekej()
c.mnoukej()

print(d.getName())
print(d.getSound())