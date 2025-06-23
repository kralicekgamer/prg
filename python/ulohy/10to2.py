i = int(input("Zadej číslo které chceš převést do 2 soustavy: "))
b = []

while i > 0:
    b.insert(0, i % 2)
    i = i // 2

print("Výsledek je: ", b)
