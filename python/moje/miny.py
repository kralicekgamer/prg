money = 100

def printPole():
    print("   A  B  C  D  E")
    for radky in range(5):
        print(str(radky + 1) + " ", end="")
        for sloupce in range(5):
            print("❓", end=" ")
        print()

def bet(money):
    bet = int(input("How much do you want to bet? "))
    if bet > money:
        print("You don't have enough money")
        return 

    bombs = int(input("How many bombs do you want to place? "))

    if bombs > 25:
        print("You can't place that many bombs")
        bet(money)
    
    money -= bet
    return bet, bombs


def placeBombs(bombs):
    radky = ["A", "B", "C", "D", "E"]
    sloupce = ["1", "2", "3", "4", "5"]

    for i in range(bombs):
        
    

def play(money, bet, bombs):
    boom = False

    while not boom:
        ("What fietd do you want to open? ")

while money > 0:
    printPole()
    print("You have " + str(money))
    bet(money)