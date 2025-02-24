x = int(input("Zadej x: "))
y = int(input("Zadej mocninu: "))

def spocitej(x, y):
    vysledek = 1

    if y < 0:
        print("Zadej kladné číslo.")
        vysledek = None
        return vysledek

    for i in range(y):
        vysledek *= x
    return vysledek

print(spocitej(x, y))
