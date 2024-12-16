def kalkulace(**kwargs):
    # linecke, rohlicky, hnizda, kokosky, koule
    # 80, 65, 90, 45, 120 / 100g 
    # -> pocet * 100 g

    x = 0

    if "linecke" in kwargs.keys():
        x += 80 * kwargs["linecke"]

    if "rohlicky" in kwargs.keys():
        x += 65 * kwargs["rohlicky"]
    
    if "hnizda" in kwargs.keys():
        x += 90 * kwargs["hnizda"]

    if "kokosky" in kwargs.keys():
        x += 45 * kwargs["kokosky"]

    if "koule" in kwargs.keys():
        x += 120 * kwargs["koule"]

    return x

print(kalkulace(linecke = 10, kokosky = 5, pernyk=5))