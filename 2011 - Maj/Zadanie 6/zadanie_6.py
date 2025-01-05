def binaryTo10(num: str,base:int) -> int:
    res = 0

    for (idx, i) in enumerate(num[::-1]):
        liczba = ord(i) - ord('0')
        res += liczba * base ** idx

    return res

def TenToOther(num: int, base: int) -> str:
    res = ''

    while num != 0:
        reszta = num % base
        num //= base

        res += str(reszta)

    res = res[::-1]

    return res

with open('liczby.txt', 'r+') as file:
    liczba_parzystych = 0
    max = [0,'']
    sum = 0

    lines = file.readlines()
    for line in lines:
        line = line[:-1]

        res = binaryTo10(line,2)
        if res % 2 == 0:
            liczba_parzystych += 1

        if res > max[0]:
            max[0] = res
            max[1] = line

        if line.__len__() == 9:
            sum += res



    print(liczba_parzystych)
    print(f"Najwieksza liczba:\nsystem 10: {max[0]}\nsystem 2: {max[1]}")
    print(f"Suma liczb o wielkosci 9: {TenToOther(sum,2)}")

