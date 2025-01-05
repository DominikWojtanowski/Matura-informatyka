def otherToTen(num: str, base: int) -> int:
    res = 0

    for (idx,letter) in enumerate(num[::-1]):
        liczbaDoDodania = ord(letter) - ord('0')
        if liczbaDoDodania >= 10:
            liczbaDoDodania = ord(letter) - ord('A')
            liczbaDoDodania += 10
        res += liczbaDoDodania * base ** idx

    return res

print(otherToTen('BA',16))
print(otherToTen('272',8))
print(186)
print(otherToTen('2232',4))
print(otherToTen('10101010',2))

def alghotitm(n: int) -> int:
    s = 1
    p = 1
    for k in range(1, n+1):
        s += p
        for i in range(1, k+1):
            p *=k
        print(s,p)

print(alghotitm(3))