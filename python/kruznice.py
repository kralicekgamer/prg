def kruznice(**kwargs):
    """
    Výpočet obsahu, obvodu nebo obojího
    """
    pi = 3.14
    r = kwargs["polomer"]
    o = kwargs["operace"]

    if o == "obsah":
        return pi * r * r
    
    if o == "obvod":
        return 2 * pi * r
    
    if o == "oboji":
        return pi * r * r, 2 * pi * r
    
print(kruznice(polomer = 69, operace = "oboji"))
