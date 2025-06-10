a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
rovnice = f"{a}x + {b} = 0"

if a == 0:
    print("Zadal jsi 0")
    exit()

x = -b / a

print(f"Kořen rovnice {rovnice}: ", x)
