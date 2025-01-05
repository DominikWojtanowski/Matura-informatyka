import math


def isPrime(asciiNum: int) -> bool:
    if asciiNum < 2:
        return False
    if asciiNum == 3:
        return True
    if asciiNum % 2 == 0:
        return False
    if asciiNum % 3 == 0:
        return  False

    i = 5
    while i * i <= asciiNum:
        if (asciiNum % (i) == 0) or (asciiNum % (i + 2) == 0):
            return False
        i += 6
    return True

def asciiSum(string: str) -> int:
    sum = 0
    for letter in string:
        sum += ord(letter)
    return sum

def asciiRosnacy(string: str) -> bool:
    for i in range(0, string.__len__() - 1):
        if ord(string[i]) >= ord(string[i + 1]):
            return False
    return True


with open("NAPIS.TXT", "r+") as readFile:
    lines = readFile.readlines()

    napisyDict = dict()
    ilePierwszych = 0
    ileRosnacych = []

    for line in lines:
        line = line[:-1]

        if isPrime(asciiSum(line)):
            ilePierwszych += 1

        if asciiRosnacy(line):
            ileRosnacych.append(line)

        if line not in napisyDict:
            napisyDict[line] = 1
        else:
            napisyDict[line] += 1

    print(ilePierwszych)
    print(ileRosnacych)
    for key, item in napisyDict.items():
        if item > 1:
            print(key, item)

