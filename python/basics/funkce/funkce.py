def vyresObjemKoule(polomer):
    return (4/3) * 3.14 * polomer ** 3 if polomer > 0 else False
    
objem = 1

while objem:
    polomer = float(input("Zadej poloměr koule: "))
    objem = vyresObjemKoule(polomer)
    print(objem)
    