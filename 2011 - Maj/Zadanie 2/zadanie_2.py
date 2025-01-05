import math


def algorytm(a: float, n: int):
    pocz_n = n
    p = 1
    b = a

    ilosc = 0

    while n > 0:
        if n % 2 != 0:
            p = p * b
            ilosc += 1
        b = b * b
        ilosc += 1
        n = n // 2

    print(f"{pocz_n}: {ilosc}")
    

for i in range(2,8):
    algorytm(2,i)


