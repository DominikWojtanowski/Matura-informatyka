def getIloscRoznychZnakow(ciag: str) -> int:
    dictRes = dict()

    iloscZnakow = 0
    for i in ciag:
        if i not in dictRes:
            dictRes[i] = 1
            iloscZnakow += 1

    return iloscZnakow

print(getIloscRoznychZnakow('ABCD'))