class Acount:
    def __init__(self, username, folowers):
        self.username = username
        self.folowers = folowers

    def add_folowers(self, pocet):
        self.folowers += pocet

        if self.folowers < 0:
            self.folowers = 0

        
    def __str__(self):
        return "Ahoj jsem " + self.username + " mám " + str(self.folowers) + " folowerů"


    def __del__(self):
        print("Uživatel " + self.username + " byl odstraněn ze systému.")

    

class VerifiedAcount(Acount):
    def __init__(self, username, folowers, color):
        super().__init__(username, folowers)  
        self.color = color

    def __str__(self):
        return "Ahoj jsem " + self.username + " mám " + str(self.folowers) + " folowerů a mám ověřený účet."

    def promote(self, pocet):
        self.folowers += pocet
        print("Uživatelovi " + self.username + " přibylo " + str(pocet) + " folowerů")


a = Acount("user1", 5)
b = VerifiedAcount("user2", 67, "blue")

print(a)
print(b)

a.add_folowers(10)
b.promote(2)

print(a)
print(b)
    

del a
del b