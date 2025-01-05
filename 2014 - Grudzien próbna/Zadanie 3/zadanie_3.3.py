from typing import List, Dict

v = [41, 196]
t = {1: 'H', 2: 'A',3: 'N',4: 'I'}
bity = 3


print(bin(v[1]))

def fun(v,t,ileBitowNaZnak):
    tmp_lista = []

    for oneBajt in v:
        liczba_bitow = 8
        while liczba_bitow != 0:
            liczba_bitow -= 1
            wartosc = (oneBajt >> liczba_bitow) & 1

            tmp_lista.append(wartosc)
            if tmp_lista.__len__() == ileBitowNaZnak:
                liczba = 0
                for (idx, i) in enumerate(tmp_lista[::-1]):
                    liczba += i * 2 ** idx
                print(t[liczba],end='')
                tmp_lista.clear()

fun([41,196],t,bity)