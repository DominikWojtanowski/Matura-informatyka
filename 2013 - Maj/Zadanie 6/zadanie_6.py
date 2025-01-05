def pierwszaCyfrJestRownaOstatniejStr(liczba: str) -> bool:
    return liczba[0] == liczba[-1]

def OctToDecAndThenBool(liczba: str) -> bool:
    res = 0
    for (idx,letter) in enumerate(liczba[::-1]):
        res += (ord(letter) - ord('0')) * 8 ** idx

    resStr = ""

    tmpRes = res
    while tmpRes > 0:
        resStr += chr(tmpRes % 10 + ord('0'))
        tmpRes //= 10

    return resStr[0] == resStr[-1]

def EZZZZFUNCTION(liczba: str) -> bool:
    for i in range(0, liczba.__len__() - 1):
        if liczba[i] > liczba[i + 1]:
            return False
    return True

with open('dane.txt', 'r+') as file:
    pierwszaCyfraJestRownaOstatniejCount = 0
    pierwszaCyfraJestRownaOstatniejDecCount = 0
    EZZZZFUNCTIONCOUNT = 0

    lines = file.readlines()
    for line in lines:
        line = line[:-1]

        if pierwszaCyfrJestRownaOstatniejStr(line):
            pierwszaCyfraJestRownaOstatniejCount += 1
        if OctToDecAndThenBool(line):
            pierwszaCyfraJestRownaOstatniejDecCount += 1
        if EZZZZFUNCTION(line):
            EZZZZFUNCTIONCOUNT += 1

    print(pierwszaCyfraJestRownaOstatniejCount)
    print(pierwszaCyfraJestRownaOstatniejDecCount)
    print(EZZZZFUNCTIONCOUNT)


