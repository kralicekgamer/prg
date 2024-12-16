import random

running = True
los = 1
ucastnici = {}


while running: 
    cmd = input("Zadej příkaz: ")

    if cmd.startswith("pridej "):
        jmeno = cmd[len("pridej "):].strip()
        if jmeno:
            ucastnici[los] = jmeno
            los += 1
        
    elif cmd == "zobraz":
        print(ucastnici)

    elif cmd == "losuj": 
        if ucastnici:
            vyherni_los = random.choice(list(ucastnici.keys()))
            print(f"Výhercem je {ucastnici[vyherni_los]} s losem číslo {vyherni_los}.")
            running = False