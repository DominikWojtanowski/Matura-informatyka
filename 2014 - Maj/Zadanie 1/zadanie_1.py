import math


def Korale(n: int, koral: str):
    if n == 1:
        koral = '-⚫-' + koral
        return koral
    elif n % 2 == 0:
        koral = '⚪-' + koral
        return Korale(n//2, koral)
    elif n % 2 == 1:
        koral = '⚫-' + koral
        return Korale((n-1)//2, koral)

def KoraleBids(n: int):
    koral = ''
    while n != 1:
        if n % 2 == 0:
            koral = '⚪-' + koral
            n //= 2
        elif n % 2 == 1:
            koral = '⚫-' + koral
            n = (n-1)//2
    koral = '-⚫-' + koral
    return koral


for i in range(1,17):
    print(i, KoraleBids(i))
    # print(i, Korale(i,''), math.floor(math.log2(i)) + 1)

