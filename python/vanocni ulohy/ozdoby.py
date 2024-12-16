def spocitatOzdoby(vyska):
    ozdoby = 0 
    v_rade = 1

    for i in range(vyska):
        ozdoby += v_rade  
        v_rade *= 2 

    return ozdoby

ozdoby = input(print("Zadej počet ozdob: "))
spocitatOzdoby(ozdoby)
