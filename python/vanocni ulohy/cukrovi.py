def dobaPeceni(druhy):
    celkovy_cas = 0
    cas = 0
    for i in range(druhy):
        cas = int(input("Zadej dobu pečení cukroví? "))
        celkovy_cas += cas
    return celkovy_cas


druhy = int(input("Kolik druhů? "))
print(dobaPeceni(druhy))
