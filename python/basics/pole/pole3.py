cisla = [10, 20, 30, 40, 50]

cisla2 = []

cisla.append(60)
print(cisla)
cisla.remove(30)
print(cisla)
cisla[0] = 5
print(cisla)
print(cisla.index(40))

x = 0

for i in cisla:
    if cisla[x] % 2 == 0:
        cisla2.append(cisla[x])
    
    x += 1

print(cisla2)