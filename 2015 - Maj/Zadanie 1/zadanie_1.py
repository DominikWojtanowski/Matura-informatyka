import math


def zapiszWPotegachDwojki(n: int) -> None:
    max_potega = math.floor(math.log2(n))

    for i in range(max_potega, -1, -1):
        ileOdjac = 2 ** i
        if n - ileOdjac >= 0:
            n -= ileOdjac
            print(ileOdjac, end=' ')
            if n == 0:
                return

def zwrocIloscPotegDwojki(n: int) -> int:
    max_potega = math.floor(math.log2(n))
    ilosc_poteg = 0

    for i in range(max_potega, -1, -1):
        ileOdjac = 2 ** i
        if n - ileOdjac >= 0:
            n -= ileOdjac
            ilosc_poteg += 1
            if n == 0:
                return ilosc_poteg



zapiszWPotegachDwojki(50)
print()
print(zwrocIloscPotegDwojki(18))