from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def whoami(self):
        pass
    
    @abstractmethod
    def max_speed(self, speed):
        pass

    @abstractmethod
    def fuel(self, f):
        pass

# Vytvoř třídu Bugatti jako potomka třídy Vehicle.
# Přepiš abstraktní metody whoami, max_speed a fuel.


class Bugatti(Vehicle):
    def whoami(self):
        print("Jsem bugaty bracho")

    def max_speed(self, speed):
        print("Moje rychlost je " + str(speed))

    def fuel(self, fuel):
        print("Moje fuel je " + str(fuel))
        
 
b = Bugatti()
b.whoami()
b.max_speed(200)
b.fuel(20)