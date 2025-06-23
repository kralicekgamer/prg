import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if (c ** 2) == (b ** 2) + math.pow(a, 2):
    print("Je pravouhly.")

else:
    print("Neni pravouhly.")

