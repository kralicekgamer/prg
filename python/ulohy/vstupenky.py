def cenaVstupenek(dite, dospely, senior):
    cena = 0
    cena += 85 * dite
    cena += 150 * dospely
    cena += 70 * senior

    if cena >= 1000:
        cena = 0.8 * cena 

    return cena

dite = int(input("Počet dětí: "))
dospely = int(input("Počet dospělých: "))
senior = int(input("Počet seniorů: "))

print(cenaVstupenek(dite, dospely, senior))
