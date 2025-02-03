from typing import List
# 1.1
# n k T[1..n] Liczba_wystapien[1..k]
# 5 10 [1,3,3,5,10] [2,2,2,3,1]
# 5 5 [5,5,5,5,5] [0,0,0,0,5]
# 10 4 [1,2,3,1,2,3,1,1,2,3] [4,3,3,0]

# Kod do sprawdzenia
def Sortowanie(n: int, k: int, T: List[int]) -> List[int]:
    Liczba_wystapien = []
    W = [0 for i in range(n)]

    for i in range(0, k):
        Liczba_wystapien.append(0)
    for i in range(0, n):
        Liczba_wystapien[T[i] - 1] += 1
    p = 0
    for j in range(k):
        for i in range(Liczba_wystapien[j]):
            W[p] = j + 1
            p += 1
    print(Liczba_wystapien)
    return W

# print(Sortowanie(5,10,[1,3,3,5,10])) # [1, 0, 2, 0, 1, 0, 0, 0, 0, 1]
# print(Sortowanie(5, 5, [5,5,5,5,5])) # [0, 0, 0, 0, 5]

## 1.2 T[i]

## 1.3

def LicznikiMod(n,k,T):
    Liczba_wystapien = [0 for i in range(k)]
    for i in range(n):
        reszta = (T[i] % k)
        Liczba_wystapien[reszta] += 1
    w = Liczba_wystapien[1]
    print(Liczba_wystapien)


print(LicznikiMod(10,2,[1, 2, 3, 4, 5, 1, 2, 3, 4, 4] ))
# w - Ilosc liczb podzielnych przez k





