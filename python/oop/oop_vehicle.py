class Vehicle:
    def __init__(self, model, speed, year):
        self.model = model
        self.speed = speed
        self.year = year

    def drive(self, driver):
        return driver + " drives this vehicle."

    def crash(self, driver):
        return self.model + " crashed by " + driver

skodovka = Vehicle("Trabant", 105, 1969)

print(skodovka.drive("Vítek"))

print(skodovka.crash("Michal"))