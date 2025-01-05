from typing import List

def tenToOther(num: int, base: int):
    res = ''

    while num > 0:
        res += str(num % base)
        num //= base

    return res[::-1]

def negateBits(bitString: str):
    return ''.join(['1' if i == '0' else '0' for i in bitString])

def U1ToTen(bitString: str) -> int:
    length = bitString.__len__() - 1

    suma = -(2 ** length) + 1 if bitString[0] == '1' else 0
    for (idx,i) in enumerate(range(bitString.__len__() -1, 0, -1 )):
        suma += (2 ** idx) if bitString[i] == '1' else 0

    return suma

def U1ToTenAlgorithm(bitLength: int, bitArr: List[int]) -> int:
    bitLengthPy = bitLength - 1
    suma = -(2 ** bitLengthPy) if bitArr[0] == 1 else 0

    for (idx, i) in enumerate(range(bitArr.__len__() - 1, 0, -1)):
        suma += (2 ** idx) if bitArr[i] == 1 else 0

    return suma + 1


res = '0' + tenToOther(42,2)
print(res)
print(negateBits(res))
print(U1ToTen(res))

U1Plus = '0100111'
U1Minus = '1001101'
print(U1ToTen(U1Plus))
print(U1ToTen(U1Minus))


print(U1ToTenAlgorithm(5, [1,0,1,1,0]))