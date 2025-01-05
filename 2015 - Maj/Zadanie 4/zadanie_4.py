from typing import Tuple

def zad4PodpunktA(line: str) -> bool:
    iloscZer = 0
    iloscJedynek = 0
    for letter in line:
        if letter == '1':
            iloscJedynek += 1
        else:
            iloscZer += 1
    if iloscZer > iloscJedynek:
        return True
    else:
        return False

def zad4PodpunktB(line: str) -> bool:
    bloki = []
    tmpblok = []
    lineLen = line.__len__()


    for i in range(0, lineLen - 1):
        if line[i] == line[i+1]:
            tmpblok.append(line[i])
        else:
            tmpblok.append(line[i])
            bloki.append(tmpblok)
            tmpblok = []
    tmpblok.append(line[lineLen-1])
    bloki.append(tmpblok)

    if bloki.__len__() != 2:
        return False
    else:
        if '1' not in bloki[0] and '0' not in bloki[1]:
            return True
        else:
            return False

def zad4PodpunktC(line: str, maxZeroes: int) -> Tuple[bool, bool, int]:
    bloki = []
    tmpblok = []
    lineLen = line.__len__()

    hasHigherZeroes = False
    hasExactZeroes = False

    newMaxZeroes = maxZeroes


    for i in range(0, lineLen - 1):
        if line[i] == line[i+1]:
            tmpblok.append(line[i])
        else:
            tmpblok.append(line[i])
            bloki.append(tmpblok)
            tmpblok = []
    tmpblok.append(line[lineLen-1])
    bloki.append(tmpblok)

    for block in bloki:
        if '1' not in block:
            zeroes = block.count('0')
            if zeroes > newMaxZeroes:
                newMaxZeroes = zeroes
                hasHigherZeroes = True
                hasExactZeroes = False
            if zeroes == maxZeroes and hasHigherZeroes == False:
                hasExactZeroes = True
    # print(f"has exact zeroes: {hasExactZeroes}")
    # print(f"has higher zeroes: {hasHigherZeroes}")
    # print(f"new max zeroes: {newMaxZeroes}")

    return (hasExactZeroes, hasHigherZeroes, newMaxZeroes)






with open('slowa.txt','r+') as file:
    lines = file.readlines()
    listaZeraWiecejNizJeden = []

    ileSpelniaPodpunkt2 = 0
    maxZeroes = 0
    iloscMaxZer = 0

    for line in lines:
        line = line[:-1]

        if zad4PodpunktA(line):
            listaZeraWiecejNizJeden.append(line)
        if zad4PodpunktB(line):
            ileSpelniaPodpunkt2 += 1

        podpunktCResult = zad4PodpunktC(line,maxZeroes)
        if podpunktCResult[0]:
            iloscMaxZer += 1
        elif podpunktCResult[1] == True:
            iloscMaxZer = 1
            maxZeroes = podpunktCResult[2]





    print(listaZeraWiecejNizJeden.__len__())
    print(ileSpelniaPodpunkt2)
    print(iloscMaxZer, maxZeroes)

zad4PodpunktB('1232233')
zad4PodpunktC('00100',2)