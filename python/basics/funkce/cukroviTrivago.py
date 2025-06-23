cukrovi = [
    ["linecká kolecka", 5, 90],
    ["vanilkové rohlicky manglove", 5, 130],
    ["vanilkové rohlicky orechove", 5, 120],
    ["vosi hnizda", 5, 100],
    ["pracny", 5, 70]
]

def kalkulace(cukrovi):
    pocitadlo = 0
    
    for c in cukrovi:
        print("Provádím kalkulaci pro", c[0] + "...")
        pocitadlo += c[1] * c[2]
    return pocitadlo

print(kalkulace(cukrovi))