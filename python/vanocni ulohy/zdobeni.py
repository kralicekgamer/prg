running = True

ozdoby = {}

while running:
    cmd = input("Zadej příkaz: ")

    if cmd.startswith("pridat "):
        barva = cmd[len("pridat "):].strip()
        if barva in ozdoby:
            ozdoby[barva] += 1
        else:
            ozdoby[barva] = 1

    elif cmd == "zobraz":
        print(ozdoby)

    elif cmd == "pocet":
        print(sum(ozdoby.values()))
        