class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return "Ahoj jsem " + self.name + " a mám roly " + self.role

    def __del__(self):
        print("Postava byla odstraněna ze hry")



class NPC(Character):
    def __init__(self, name, role, skill):
        super().__init__(name, role)
        self.skill = skill

class Player(Character):
    def __init__(self, name, role, control_device):
        super().__init__(name, role)
        self.control_device = control_device


p = Player("Michal", "King", "Kontroler")
n = NPC("Vítek", "Raigbater", 1)

print(p)
print(n)