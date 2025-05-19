jmena = ["Anna", "Tom", "Eva", "Martin", "Lukas"]
jmena2 = []

if "Eva" in jmena:
    print("Eva je v listu.")

jmena.insert(0, "Klara")

print(jmena)

jmena.insert(1, "Tomas")
print(jmena)
jmena.remove(jmena[-1])
print(jmena)

for i in jmena:
    if i == "Martin":
        martin = 0
        martin = martin + 1
        print(f"Martin je v listu: {martin}")

x = 0

for i in jmena:
    if len(jmena[x]) >= 4:
        jmena2.append(jmena[x])
    
    x += 1


print(jmena2)