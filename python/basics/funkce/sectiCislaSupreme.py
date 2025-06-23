def sectiCisla(**kwards):
    soucet = 0 
    for klic, hodnota in kwards.items():
        soucet += hodnota

    return soucet

print(sectiCisla(a=1, kocka=3, pes=9, rybicky=25))
