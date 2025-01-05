from typing import Tuple, List

def getNumLength(n: int) -> int:
    len = 1
    while n >= 10:
        n //= 10
        len += 1
    return len

def armstrongNum(n: int) -> int:
    potega = getNumLength(n)

    sum = 0
    while n >= 10:
        sum += (n % 10) ** potega
        n //= 10
    sum += n ** potega
    return sum

def armstrongNumList(n: int) -> Tuple[List,int]:
    potega = getNumLength(n)
    list = []

    sum = 0
    while n >= 10:
        sum += (n % 10) ** potega
        list.append(n % 10)
        n //= 10
    sum += n ** potega
    list.append(n)
    return (list,potega)

def potega(a, n):
    return a ** n

def lista(k: int):
    list = []

    while k >= 10:
        list.append(k % 10)
        k //= 10
    list.append(k)

    return list

def armstrongNumZad(k: int) -> str:
    len = getNumLength(k)

    list = lista(k)
    sum = 0

    for i in list:
        sum += potega(i, len)

    return 'PRAWDA' if sum == k else "FAŁSZ"




print(armstrongNum(6) == 6)
print(armstrongNum(407) == 407)
print(armstrongNum(2278) == 2278)

print(armstrongNumList(54321))

print(armstrongNumZad(153))