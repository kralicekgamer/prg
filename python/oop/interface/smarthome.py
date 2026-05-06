from abc import ABC, abstractmethod


class SmartHome(ABC):
    @abstractmethod
    def getProperties(**kwargs):
        pass
    
    @abstractmethod
    def setProperties(**kwargs):
        pass


class Lights(SmartHome):
    def __init__(self, name, room, type_of_light, luminosity, color):
        self.name = name
        self.room = room
        self.type_of_light = type_of_light
        self.luminosity = luminosity
        self.color = color

    def getProperties(self, **kwargs):
        if kwargs == {}:
            return self.__dict__
        else:
            properties = {}
            for key in kwargs:
                properties[key] = getattr(self, key)
            return properties

    def setProperties(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


svetlo = Lights("Svetlo", "Loznice", "LED", "200", "red")

# potrebujeme predat pozicni argument. je jedno co predame.
print(svetlo.getProperties(name=True, color = True))

svetlo.setProperties(name="Svetlo2")

print(svetlo.getProperties())


class Router(SmartHome):
    def __init__(self, name, room, ip, supported_frequencies, mesh):
        self.name = name
        self.room = room
        self.ip = ip
        self.supported_frequencies = supported_frequencies
        self.mesh = mesh

    def getProperties(self, **kwargs):
        if kwargs == {}:
            return self.__dict__
        else:
            properties = {}
            for key in kwargs:
                properties[key] = getattr(self, key)
            return properties

    def setProperties(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


router = Router("Michal", "Loznice", "192.168.1.100", ["2,4", "5"], True)
print(router.getProperties())

