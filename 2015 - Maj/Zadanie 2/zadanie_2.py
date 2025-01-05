from typing import List, Tuple
def strategiaTrzecia(mk: int, n: int, MASA: List[int], CENA: List[int]) -> Tuple[List[int], int]:
    w = 0
    K = [0] * n
    j = 0
    for i in range(n-1,-1,-1):
        if mk - MASA[j] >= 0:
            mk -= MASA[j]
            K[j] = 1
            w += 1
        if mk == 0:
            break
        j += 1
    return (K,w)

MASA = [8,4,1,2,3,5,1]
CENA = [320,152,37,70,99,155,30]

print(strategiaTrzecia(10,7,MASA, CENA))

