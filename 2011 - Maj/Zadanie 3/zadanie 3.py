def to_10base(num: str, base: int):
    res = 0

    for (idx,i) in enumerate(num[::-1]):
        liczba = int(ord(i) - ord('0'))
        if liczba >= 10:
            liczba = int(ord(i) - ord('A')) + 10
        res += liczba * base ** idx

    return res

print(f"{to_10base('21202',3)} wazne")
print(to_10base('D1',16))
print(to_10base('321',8))
print(to_10base('10110001',2))
print(to_10base('211',10))