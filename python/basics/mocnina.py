x = int(input("Zadej x: "))
y = int(input("Zadej mocninu: "))

def spocitej(x, y):
    vysledek = 1
    for i in range(y):
        vysledek *= x
    return vysledek

print(spocitej(x, y))
