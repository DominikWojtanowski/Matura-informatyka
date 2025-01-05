import math


def getMaxY(x,r) -> int:
    return int(math.sqrt(r * r - x * x))

r = 1.12223

r_zaokr = int(r)
pocz = 1 + 4 * r_zaokr

cwiartka = 0

for i in range(1, r_zaokr+1):
    cwiartka += getMaxY(i,r)

print(pocz + cwiartka * 4)