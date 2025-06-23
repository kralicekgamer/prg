import random

a = []

for i in range(20):
    a.append(random.randint(1, 50))

print(a)

x = int(input("Zadej číslo: "))

b = 0

if x in a:
    for ii in a:
        if ii == x:
            b += 1

    print("Toto číslo tam je", b)