class Player:
    count = 0

    def __init__(self, nick, age):
        self.nick = nick
        self.age = age
        Player.count += 1


    def getInstanceAmounth():
        return Player.count

    def getPlayer(self):
        return f"Hráč se jmenuje {self.nick} stáří učtu je {self.age}."


    def __del__(self):
        Player.count -= 1


p = Player("Nigga", 12)

print(Player.getInstanceAmounth())

print(p.getPlayer())

del p

print(Player.getInstanceAmounth())