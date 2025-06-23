def posunX(bod, posun_X) -> list:
    return [bod[0] + posun_X, bod[1]]


def posunY(bod, posun_Y) -> list:
    return [bod[0] + posun_Y, bod[1]]


def posunBod(bod, posun_X, posun_Y) -> list:
    bod_po_posunu_X = posunX(bod, posun_X)  
    return posunY(bod_po_posunu_X, posun_Y) 


A = [3, 7]

B = posunX(A, -2)
print(B)

C = posunY(A, -5)
print(C)

D = posunBod(A, -2, 5)
print(D)
