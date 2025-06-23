A = [5, 2]
B = [6, 5]

def vzdalenostBodu(A, B) -> float:
    AxBx = abs(A[0] - B[0])
    AyBy = abs(A[1] - B[1])  

    return (AxBx ** 2 + AyBy ** 2) ** 0.5

print(vzdalenostBodu(A, B))
print(vzdalenostBodu([1, 9], [9, 5]))