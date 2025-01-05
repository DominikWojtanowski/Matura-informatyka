def to_ten(num: str, base: int) -> int:
    res = 0

    for (idx,i) in enumerate(num[::-1]):
        liczba = (ord(i) - ord('0'))
        if liczba >= 10:
            letter = str(i).upper()
            liczba = (ord(letter) - ord('A'))
            res += (liczba + 10) * base ** idx
        else:
            res += liczba * base ** idx

    return res

def to_binary(num: int):
    res = ''
    while num != 0:
        res += str(num % 2)
        num //= 2
    return res[::-1]

print(f"Do porownania: {to_ten('1E',16)}")
print(to_ten('101010',2))
print(to_ten('36',8))
print(to_ten('1110',3))
print(to_ten('30',10))

# sum = to_ten('1110',2) + to_ten('10',2)
# sub = to_ten('1110',2) - to_ten('10',2)
# dzielenie = to_ten('1110',2) // to_ten('10',2)
# mnozenie = to_ten('1110',2) * to_ten('10',2)
# print(to_binary(sum), to_binary(sub), to_binary(dzielenie), to_binary(mnozenie))