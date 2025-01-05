from typing import Tuple, List

def tabliczka(granica: int) -> List[List[int]]:
    res: List[List[int]] = []
    for i in range(1, granica + 1):
        tmp: List[int] = []
        for j in range(1, granica + 1 - (i - 1)):
            tmp.append(j * i)
        res.append(tmp)

    return res

def przekatnaSum(tab: List[List[int]], nrPrzekatnej: int) -> int:
    sum = 0
    szerokosc = tab.__len__()
    ktoraZaczynamy = nrPrzekatnej - 1
    noramlnyIndex = -tab[ktoraZaczynamy].__len__()

    for i in range(0,ktoraZaczynamy + 1):
        sum += tab[i][noramlnyIndex]

    return sum

print(tabliczka(7))
print(przekatnaSum(tabliczka(8),8))