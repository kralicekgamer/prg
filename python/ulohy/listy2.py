cisla = [4, 7, 2, 9, 10, 15, 8]

liche = 0
sude = 0

for i in range(len(cisla)):
    if cisla[i] % 2 == 0:
        sude += 1
        print(f"Číslo {cisla[i]} je sudé")

    else:
        liche += 1
        print(f"Číslo {cisla[i]} je liché")

print(f"Lichých čísel je {liche} a sudých {sude}")