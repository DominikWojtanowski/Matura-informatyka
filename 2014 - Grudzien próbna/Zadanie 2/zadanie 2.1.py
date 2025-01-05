def otherToTen(n: str, base: int) -> int:
    sum = 0

    for idx, i in enumerate(n[::-1]):
        sum += int(i) * base ** idx
    return sum

def tenToOther(n: int, to: int):
    res: str = ''

    if n == 0:
        return '0'

    while n > 0:
        liczba = n % to

        do_dodania = chr(ord('A') + liczba - 10) if liczba >= 10 else str(liczba)

        res = do_dodania + res
        n //= to

    return res



a = '1001001' # 2
b = '211' # 9
c = '211' # 8

print(otherToTen(c,8))

print(otherToTen(a,2) + otherToTen(b,9) - otherToTen(c,8))
print(tenToOther(otherToTen(c,8),16))
