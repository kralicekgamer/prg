import random

nahodna = []
nahodna2 = []

for i in range(100):
    nahodna.append(random.randint(1, 100))

print(nahodna)

i = 0
while i < 100:
    cislo = random.randint(1, 100)
    if cislo not in nahodna2:
        nahodna2.append(cislo)
        i += 1

nahodna3 = random.sample(range(1,101), 100)

print(nahodna)
print("-")
print(nahodna2)
print("-")
print(nahodna3)
print("-")
nahodna2.sort(reverse=False)
print(nahodna2)
