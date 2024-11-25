Ax = 5
Bx = 8
Ay = 12
By = 5

def vzdalenostBodu(Ax, Ay, Bx, By) -> float:
    AxBx = abs(Ax - Bx)
    AyBy = abs(Ay - By)  

    return (AxBx ** 2 + AyBy ** 2) ** 0.5


print(vzdalenostBodu(Ax, Bx, Ay, By))
print(vzdalenostBodu(15, 12, 18, 5))
