def prumernaRychlost(draha, cas):
    rychlost = draha / cas
    return rychlost

draha = float(input("Zadejte dráhu(m): "))
cas = float(input("Zadejte čas(s): "))
print(prumernaRychlost(draha, cas), "m/s")

