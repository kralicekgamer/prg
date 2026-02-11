class Projektor:
    def zapnout(self):
        print("Projektor zapnut")

    def vypnout(self):
        print("Projektor vypnut")

    def nastavit_vstup_hdmi(self):
        print("Projektor: HDMI vstup nastaven")


class Reproduktory:
    def zapnout(self):
        print("Reproduktory zapnuty")

    def vypnout(self):
        print("Reproduktory vypnuty")

    def nastavit_hlasitost(self, hodnota):
        print(f"Reproduktory: hlasitost nastavena na {hodnota}")


class Platno:
    def spustit_dolu(self):
        print("Plátno spuštěno dolů")

    def vytahnout_nahoru(self):
        print("Plátno vytaženo nahoru")

class ProjektorovySystem:
    def __init__(self):
        self.projektor = Projektor()
        self.reproduktory = Reproduktory()
        self.platno = Platno()

    def zapnout_prezentaci(self):
        print("\n--- Zapínám prezentaci ---")
        self.platno.spustit_dolu()
        self.projektor.zapnout()
        self.projektor.nastavit_vstup_hdmi()
        self.reproduktory.zapnout()
        self.reproduktory.nastavit_hlasitost(5)

    def vypnout_prezentaci(self):
        print("\n--- Vypínám prezentaci ---")
        self.projektor.vypnout()
        self.reproduktory.vypnout()
        self.platno.vytahnout_nahoru()


if __name__ == "__main__":
    system = ProjektorovySystem()

    system.zapnout_prezentaci()
    system.vypnout_prezentaci()

