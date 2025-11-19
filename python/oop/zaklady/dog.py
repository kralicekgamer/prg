class Dog:
    count = 0
    money = 0

    def __init__(self, race, sex, age, price):
        self.race = race
        self.sex = sex
        self.age = age
        self.price = price
        Dog.count += 1

    def __del__(self):
        Dog.count -= 1
        Dog.money += self.price

shiba_inu = Dog("Shiba Inu", "M", 1, 690)
shi_tzu = Dog("Shi Tzu", "F", 2, 420)
print(shiba_inu.age)
print(Dog.count)
del shiba_inu
print(Dog.count)
print(Dog.money)