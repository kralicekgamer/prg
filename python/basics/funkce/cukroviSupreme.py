def kalkulace(**kwargs):
    # [<mnozstvi>, <cena za 100g>]
    pocitadlo = 0

    for klic, hodnota in kwargs.items():
        print("Počítam cenu za: ", klic)
        pocitadlo += hodnota[0] * hodnota[1]

    return pocitadlo

print(kalkulace(linecke = [5, 80], rohlicky = [7.5, 65], pernicky = [10, 75]))