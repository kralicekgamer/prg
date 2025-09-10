# ============================================
# Přehled metod objektu třídy list v Pythonu
# ============================================
# append(x)        – přidá prvek x na konec seznamu
# extend(iter)     – rozšíří seznam o všechny prvky zadaného iterovatelného objektu
# insert(i, x)     – vloží prvek x na pozici i
# remove(x)        – odstraní první výskyt prvku x
# pop([i])         – odstraní a vrátí prvek na pozici i (výchozí je poslední)
# clear()          – vyprázdní seznam
# index(x[, start[, end]]) – vrátí index prvního výskytu prvku x
# count(x)         – vrátí počet výskytů prvku x
# sort(key=None, reverse=False) – seřadí seznam na místě
# reverse()        – otočí pořadí prvků v seznamu
# copy()           – vrátí mělkou kopii seznamu

# ============================================
# Zadání k procvičení
# ============================================

# 1. Vytvoř prázdný seznam a postupně do něj pomocí append() přidej pět čísel zadaných uživatelem.
cisla = []

for i in range(5):
    cislo = input("Zadej cislo: ")
    cisla.append(cislo)

print(cisla)

# 2. Zeptej se uživatele na pět jmen, ulož je do seznamu a následně seznam seřaď abecedně.
jmena = []

for i in range(5):
    jmeno = input("Zadej jmeno: ")
    jmena.append(jmeno)
    jmena.sort(key=str.lower) # ! nevedel sem key

print(jmena)

# 3. Vytvoř seznam čísel 1–10, pomocí pop() postupně odstraňuj poslední prvky, dokud není seznam prázdný.
cisla_prvky = []

for i in range(1, 11): 
    cisla_prvky.append(i)
    

for i in reversed(range(len(cisla_prvky))):
    cisla_prvky.pop(i)
    print(cisla_prvky) 
    

# 4. Máš seznam čísel. Pomocí for a if zjisti, kolik čísel je sudých (využij count() pro kontrolu).
sude_a_liche =[1, 2, 5, 6, 11]

for i in range(len(sude_a_liche)):
    if sude_a_liche[i] % 2 == 0:
        print(f"Cislo {sude_a_liche[i]} je sude")

    else:
        print(f"Cislo {sude_a_liche[i]} je liche")

# 5. Vytvoř seznam měst, přidej jedno město na začátek pomocí insert().
mesta = ["Liberec", "Praha", "Varndorf"]
mesta.insert(0, "Ústí")
print(mesta)

# 6. Vytvoř seznam [3, 1, 4, 1, 5, 9], zjisti kolikrát se v něm vyskytuje číslo 1 (metoda count).
jednicka = [3, 1, 4, 1, 5, 9]
print(jednicka.count(1))

# 7. Ze seznamu slov odstraň jedno konkrétní slovo (metoda remove). Pokud tam není, vypiš hlášku.
print(mesta)
mesto_remove = input("Zadej mesto pro smazani: ")
if mesto_remove not in mesta:
    print("Mesto neni v seznmu")

else: 
    mesta.remove(mesto_remove)
print(mesta)


# 8. Zeptej se uživatele na seznam čísel, seřaď je sestupně pomocí sort(reverse=True).
cisla_b = []
cisling = True

while cisling:
    cislo_b = input("Zadej cislo (exit pro konec): ")
    if cislo_b == "exit":
        cisling = False
    else:
        cisla_b.append(cislo_b)

cisla_b.sort(reverse=True)
print(cisla_b)

# 9. Vytvoř seznam a pomocí while cyklu vypisuj a zároveň odstraňuj první prvek (pop(0)), dokud není prázdný.
cisla_while = [5, 8, 6, 1, 6, 7]
cisla_whiling = True

while cisla_whiling:
    cisla_while.pop(0)
    print(cisla_while)

    if cisla_while == []:
        cisla_whiling = False

# 10. Vytvoř seznam náhodných čísel a otoč jeho pořadí metodou reverse().
nahodna = [5, 8, 5, 2, 7, 6]
nahodna.reverse()
print(nahodna)

# 11. Vytvoř seznam čísel, zkopíruj jej metodou copy() a s kopií dále pracuj (např. přidej prvky).
seznam_copy = [5, 7, 3, 6, 7, 3]
seznam_copy_new = seznam_copy.copy()

seznam_copy_new.pop(0)
print("Puvodni seznam", seznam_copy)
print("Novy seznam", seznam_copy_new)

# 12. Napiš program, který do seznamu ukládá vstupy uživatele, dokud nezadá „stop“. Poté seznam vypiš.
vstupy = []
zadaving = True

while zadaving:
    vstup = input("Zadej veci do seznamu (stop pro konec): ")
    if vstup == "stop":
        zadaving = False

    else:
        vstupy.append(vstup)

print(vstupy)

# 13. Vytvoř seznam čísel a najdi index určitého čísla metodou index(). Pokud číslo neexistuje, vypiš hlášku.
indexy = [5, 6, 7, 6, 9, 4, 2, 0]

index_input = int(input("Zadej cislo na index: "))

if index_input not in indexy:
    print("Cislo neni v seznamu")

else:
    print(indexy.index(index_input))

# 14. Máš seznam [2, 4, 6, 8]. Přidej do něj pomocí extend() další seznam [1, 3, 5, 7].
seznam_a = [2, 4, 6, 8]

seznam_b = [1, 3, 5, 7]


seznam_a.extend(seznam_b)

print(seznam_a)

# 15. Vytvoř seznam, do kterého budeš ukládat jen ta čísla od uživatele, která jsou větší než 10 (if + append).
bigering = True
big = []

while bigering:
    big_input = input("Zadej cislo (exit pro konec): ")
    if big_input == "exit":
        bigering = False

    elif int(big_input) < 10: 
        print("Cislo je mensi nez 10")
        pass
    
    else:
        big.append(big_input)

print(big)

# 16. Máš seznam známek (1–5). Pomocí for spočítej průměr a vypiš jej.
znamky = [1, 4, 5, 1, 2, 4, 3]
prumer = 0

for i in range(len(znamky)):
    prumer = prumer + znamky[i] 

print(prumer / len(znamky))

# 17. Vytvoř seznam čísel a vymaž všechny prvky metodou clear(). Ověř, že je prázdný.
znamky.clear()
print(znamky)


# 18. Generuj náhodná čísla do seznamu, dokud se neobjeví číslo 7. Poté cyklus while ukonči a vypiš seznam.
import random

nahoding = True
nahodna_b = []

while nahoding:
    nahodne_add = random.randint(0, 10)

    nahodna_b.append(nahodne_add)

    if nahodne_add == 7:
        nahoding = False
    print(nahodna_b)
