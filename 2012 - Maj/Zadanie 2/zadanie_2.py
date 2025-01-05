def isOsiagalna(liczba: int):
    max_sum = maxOsiagalna(liczba)

    poczatek = liczba
    koniec = liczba - max_sum

    for i in range(poczatek, koniec - 1, -1):
        # print(i, sumLiczb(i))
        suma = sumLiczb(i)
        if poczatek == i + suma:
            return (True, i, suma)
    return (False,0,0)

def maxOsiagalna(liczba:int):
    pocz_liczba = str(liczba)

    max_sum = pocz_liczba
    if max_sum[0] >= '1':
        max_sum = chr(ord(pocz_liczba[0]) - 1) + ''.join(['9' for i in range(1,max_sum.__len__())])
    else:
        max_sum = ''.join(['9' for i in range(1,max_sum.__len__())])

    sum = 0
    for i in max_sum:
        sum += ord(i) - ord('0')

    return sum

def sumLiczb(liczba: int):
    # print(liczba)
    sum = 0
    base = 10
    i = 1
    while liczba != 0:
        sum += liczba % 10
        liczba //= 10
        i += 1
    return sum




poczatek = 1000
koniec = 9999

# print(sumLiczb(505))
for i in range(koniec, poczatek - 1, -1):
    wynik = isOsiagalna(i)
    if wynik[0] == True:
        print(wynik, i)