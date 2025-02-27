from typing import Tuple

def algorytm(n: int) -> Tuple[int,int,int]:
    index = 0
    p1: int = 1
    suma: int = 0
    for k in range(1,n+1):
        index += 1
        p1 = p1 * n
        p2: int = 1
        for i in range(1,n+1):
            index += 1
            p2 = p2 * k
        suma = suma + p1 + p2
        index += 2

    print(index)
    return (p1, p2, suma)

def algorytm_modifikacja(n: int) -> Tuple[int,int,int]:
    index = 0
    p1: int = 1
    suma: int = 0
    for k in range(1,n+1):
        index += 1
        p1 = p1 * n
        p2: int = 1
        for i in range(1,k+1):
            p2 = p2 * i

        print(p2,p1)
        suma = suma + p1 + p2
        index += 2

    print(index)
    return (p1, p2, suma)

print(algorytm_modifikacja(3))
# 5
# 10
# 15
