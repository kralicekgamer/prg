import random

def vyresObjemKoule(polomer):
    return (4/3) * 3.14 * polomer ** 3 if polomer > 0 else False
    

i = 0


while True:
    if i < 10:
        polomer = random.randint(1, 1000)
        vyresObjemKoule(polomer)
        print(polomer)
        i = i + 1
        
    else:
        exit()
    