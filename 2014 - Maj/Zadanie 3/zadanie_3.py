import math


def fun(n: int):
    if n == 1:
        suma = 1
    else:
        suma = 1 + n
        i = n - 1

        while i > 1:
            suma = 1 + i * suma
            i = i - 1

        return suma
print(fun(4), fun(6))

print(hex(int('101011111100',2)))

print(math.gcd(31,42))
print(math.lcm(31,42))

print(math.gcd(1310,524))
print(math.lcm(1310,524))