def baseToTen(num: str, base: int) -> int:
    res: int = 0

    # 81(8) -> 1 * 8 ^ 0 + 8 * 8 ^ 1
    for idx, i in enumerate(num[::-1]):
        value = (ord(i) - ord('0'))
        if value >= 10:
            value = (ord(i) - ord('A')) + 10
        value = value * base ** idx

        res += value

    return res


def baseToOther(num: str, base: int, to: int) -> str:
    newNum = baseToTen(num, base)
    res = ""

    while newNum / to != 0:
        value = newNum % to
        newNum //= to

        if value >= 10:
            value = chr(ord('A') + (value - 10))
        res += str(value)

    return res[::-1]

def f(num: int) -> float:
    if num == 1:
        return 4
    else:
        return 1 / (1 - f(num - 1))





print(f"{baseToTen('CB', 16)} <--- poprawny wynik")
print(baseToTen('10101111',2))
print(baseToTen('313',8))
print(baseToTen('3120',4))
print(203)


## podpunkt 2

print(f'')
print(f(8))
print(f(9))
print(f(10))
print(f(100))

## podpunkt 3

print('FPPF')

#### 1.5

num = '11111111111111111111'
print(baseToOther(num,2,4).__len__())
print(baseToOther(num,2,8).__len__())
print(baseToOther(num,2,16).__len__())
print(baseToOther(num,2,10).__len__())

