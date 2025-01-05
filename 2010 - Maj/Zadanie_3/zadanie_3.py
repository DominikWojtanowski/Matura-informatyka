# print(int('1000',16))
# # print(int('34522',5))
# print(int('10000',8))

def konwertowanie_na_dziesiatkowy(number: str, base: int):
    res = 0

    for i in range(number.__len__()):
        if ord(number[-(i + 1)]) - ord('0') < 10:
            res += (ord(number[-(i + 1)]) - ord('0')) * base ** i
        else:
            res += ((ord(number[-(i + 1)].upper()) - ord('A')) + 10) * base ** i

    return res

def konwertowanie_na_dany_system_liczbowy_z_dziesiatkowego(number: int, base: int):
    res = ''

    while number != 0:
        reszta = number % base
        number = number // base

        if reszta >= 10:
            res = chr(ord('A') + (reszta - 10)) + res
        else:
            res = str(reszta)

    return res

print(konwertowanie_na_dziesiatkowy('1000',16))
print(konwertowanie_na_dziesiatkowy('34522',5))
print(konwertowanie_na_dziesiatkowy('4096',10))
print(konwertowanie_na_dziesiatkowy('10000',8))
