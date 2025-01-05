from typing import Tuple
def silnia(n) -> int:
    if n == 1:
        return 1
    else:
        return silnia(n-1) * n

def ilosc_mnozen(n) -> int:
    return sum(range(n))

def inny_wzor_ilosc_mnozen(n) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 3

    iter_wynik = (1 + (n-1) * (n+1))

    n -= 1

    while n > 3:
        iter_wynik = (1 + (n-1) * iter_wynik)
        n -= 1

    return 1 + 2 * iter_wynik











