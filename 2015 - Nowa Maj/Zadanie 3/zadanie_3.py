def NWD(a:int,b:int) -> int:
    if b == 0:
        return a
    else:
        r = a % b
        return NWD(b,r)

def extendedNWD(a: int, b: int):
    if b == 0:
        return a, 1, 0
    else:
        nwd, x1, y1 = extendedNWD(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return nwd, x, y


# print(NWD(24,36))
# print(extendedNWD(24,36, 0, 0))
print(extendedNWD(231,30))