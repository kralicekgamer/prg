A = {"x": 0, "y": 3}
B = {"x": 5, "y": 8}

def vzdalenostBodu(A, B) -> float:
    AxBx = abs(A["x"]) - abs(A["y"])
    AyBy = abs(B["x"]) - abs(B["y"])

    return (AxBx ** 2 + AyBy ** 2) ** 0.5

print(vzdalenostBodu(A, B))
print(vzdalenostBodu({"x": 5, "y": 7}, {"x": 8, "y": 6}))