from typing import List

def isTriada(a,b,c):
    print(a,b,c)
    return (a + b > c) and (a + c > b) and (b + c > a)

def triadyC(n: int, c: List[int]) -> List[int]:
    """
    :param n: n >= 2
    :param c: ciag liczb dodatnich c1 < c2
    :return: triady c
    """

    a = c[0]
    b = c[1]

    triady: List[int] = []

    for i in range(2, n):
        if isTriada(a,b,c[i]):
            triady.append(c[i])

    return triady
print(triadyC(21,[5,15,2,3,5,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]))
