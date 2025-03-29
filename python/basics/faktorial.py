def faktorial(n):
    if n == 0:
        return 1
    
    vysledek = n

    for i in range(n):
        if n == 1:
            return vysledek
        
        n = n - 1

        vysledek = vysledek * n
        

print(faktorial(5))
