# třída
class Lady:
    # konstruktor
    def __init__(self, height, weight, age, sex, status, skin):
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.status = status
        self.skin = skin

    # metoda
    def kolik_je(self):
        """Odpoví kolik jí je let"""
        print(f"Ahoj je mi {self.age}.")

    def dominance(self):
        print("Neser mě a jdi makat na pole.")

    def submise(self):
        return "Budu tvoje poslušná kurvička"

    def pegging(self):
        print("Pokračuj dál a začnu tě pegovat.")

# PRVNI OBJEKT
black_lady = Lady(165, 55, 17, "F", "single", "black")

# -- vytisknout vek --
print(black_lady.age)

# zavolat metodu veku
black_lady.kolik_je()

# tiskne se v metode
black_lady.dominance()

# vyhrozuje
black_lady.pegging()

# kdyz se vrati, musi se vytisknout
print(black_lady.submise())


# DRUHY OBJEKT
white_lady = Lady(210, 60, 33, "F", "single", "white")