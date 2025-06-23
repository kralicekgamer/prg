def pocitej(**kwargs):
    c = kwargs["cisla"]
    o = kwargs["operace"]


    if o == "prumer":
        return sum(c)/len(c)

    if o == "maximum":
        return max(c)
    
    if o == "minimum":
        return min(c)
    

print(pocitej(cisla = [5, 2, 4, 5], operace = "maximum"))
