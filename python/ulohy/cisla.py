import random

nahodne_cislo = random.randint(0, 100)
historie_pokusu = []


while True:
    tip = int(input("Co si myslíš že je to za číslo? "))
    historie_pokusu.append(tip)

    if tip > nahodne_cislo:
        print(f"Číslo je menší než {tip}.")

    elif tip < nahodne_cislo:
        print(f"Číšlo je větší než {tip}.")

    elif tip == nahodne_cislo:
        pokus = len(historie_pokusu)
        print(f"Uhádnul jsi číslo. Úhádnul jsi ho na {pokus}. Číslo je {tip}.")
        print(f"Historie pokusů: {historie_pokusu}")
        break

    else:
        print("Lofas error. ")

    