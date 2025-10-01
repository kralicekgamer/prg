class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def predstaveni(self):
        print(f"Ahoj jsem {self.name}.")

    def vek(self):
        print(f"Je mi {self.age}.")

class Pes(Animal):
    def __init__(self, name, age, plemeno):
        super().__init__(name, age) 
        self.plemeno = plemeno

    def stekej(self):
        print("HAF")

    def jakePlemeno(self):
        print(f"Moje plemeno je {self.plemeno}")

class Lev(Animal):
    def __init__(self, name, age, sigma):
        super().__init__(name, age)

    def jsemSigma(self):
        if self.jsemSigma:
            print("Jsem veliká Sigma")

        else: 
            print("Nejsem sigma")


muj_pes = Pes("Michal", 16, "Zlatý retrývr")
muj_pes.predstaveni()
muj_pes.stekej()


muj_lev = Lev("Vítek", 16, True)
muj_lev.predstaveni()
muj_lev.jsemSigma()