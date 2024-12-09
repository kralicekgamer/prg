def sectiCisla(*args):
    soucet = 0
    for arg in args:
        # soucet = soucet + arg
        soucet += arg # operátor příčítání
    return soucet


def sectiCisla2(a=0, b=0):
    return a + b


print(sectiCisla(5, 7, 12))
print(sectiCisla(5, 8, 5, 6, 1, 2))
print(sectiCisla())

print(sectiCisla2(5, 7))

