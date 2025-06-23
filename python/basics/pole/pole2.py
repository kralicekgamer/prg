# Vytvoříme seznam s čísly od 0 do 100
pole = [i for i in range(101)]

# Vytvoříme nový seznam obsahující každý druhý prvek
druhe_prvky = [pole[i] for i in range(0, len(pole), 2)]

# Vypíšeme všechny prvky najednou
for prvek in druhe_prvky:
   print(prvek)