from typing import List

def sito_eratostenesa(n: int) -> List[int]:
    if n == 1:
        return [1]
    list = [0 for i in range(0,n+1)]

    i = 2
    while i < n:

        if list[i] == 0:
            j = 2 * i

        while j <= n:
            list[j] = 1
            j += i

        i += 1
    return list

def sito_eratostenesa_inny_zwrot(n: int) -> List[bool]:
    if n == 1:
        return [1]
    list = [0 for i in range(0,n+1)]

    i = 2
    while i < n:

        if list[i] == 0:
            j = 2 * i

        while j <= n:
            list[j] = 1
            j += i

        i += 1
    return [True if i == 0 else False for i in list]


print(sito_eratostenesa_inny_zwrot(4))

def nie_podzielne(N: int, M: int, A: List[int]) -> List[int]:
    jest_podzielne = False
    # A = sorted(A)

    if N == 2:
        for n in A:
            if 2 % n == 0:
                jest_podzielne = True
        return [2] if jest_podzielne == False else []

    list = [0 for i in range(0, N + 1)]
    print(len(list))

    for i in range(1, M+1):
        # print(i)
        if i >= len(A):
            break
        # print(i)
        # print(f"{i}: {A[i]}")
        j = A[i]
        while j <= N:
            list[j] = 1
            j += A[i]

    # print(list)
    return [i for i in range(len(list)) if list[i] == 0 and i != 0 and i != 1]
    # return [True if i == 0 else False for i in list]

print(nie_podzielne(20,7,[2,2,3]))

def zmodyfikowany_algorytm(N: int) -> List[int]:
    T = [0 for i in range(N+1)]

    i = 2
    while i < N:
        if T[i] == 0:
            j = 2 * i
            while j <= N:
                T[j] += 1
                j += i
        i += 1

    return T

def checkIfIsPrime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, n, 6):
        if i * i >= n:
            break
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True








