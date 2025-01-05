def otherToTen(num: str, fromBase: int):
    res = 0

    for (idx,i) in enumerate(num[::-1]):
        liczba = ord(i) - ord('0')
        if liczba > 9:
            liczba = ord(i) - ord('A') + 10
        res += liczba * fromBase ** idx

    return res

def tenToOther(num: int, toBase: int):
    res = ''

    while num != 0:
        liczba = num % toBase

        if liczba > 9:
            liczba = chr(ord('A') + liczba - 10)
        else:
            liczba = str(liczba)

        num //= toBase

        res += liczba

    return res[::-1]


print(otherToTen('1032',4) * otherToTen('131',4))

print(tenToOther(2262,10))
print(tenToOther(2262,16))
print(tenToOther(2262,8))
print(tenToOther(2262,2))


