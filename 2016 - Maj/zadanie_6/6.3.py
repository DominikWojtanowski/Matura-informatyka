def znajdzKlucz(literaSlowa, innaLiteraSlowa):
    klucz = 0
    if ord(innaLiteraSlowa) - ord(literaSlowa) < 0:
        return ord('Z') - ord(literaSlowa) + (ord(innaLiteraSlowa) - ord('A') + 1)
    else:
        return ord(innaLiteraSlowa) - ord(literaSlowa)


def czyPoprawne(slowo, inneSlowo):
    res = ""
    klucz = 0
    if ord(inneSlowo[0]) - ord(slowo[0]) < 0:
        klucz = (ord('Z') - ord(slowo[0])) + (ord(inneSlowo[0]) - ord('A') + 1)
    else:
        klucz = ord(inneSlowo[0]) - ord(slowo[0])

    for idx, i in enumerate(slowo, start=0):
        if klucz != znajdzKlucz(innaLiteraSlowa=inneSlowo[idx],literaSlowa=i):
            return False
    return True





with open('dane_6_3.txt','r') as file:
    lines = [line.replace('\n','').split(' ')for line in file.readlines()]
    with open('wyniki_6_3.txt','w') as toWrite:
        for line, otherLine in lines:
            if czyPoprawne(line,otherLine) == False:
                toWrite.write(f"{line}\n")
# print(czyPoprawne("ZAWISLAK","EFBNXQFP"))

# for i in range(65,91):
#     print(chr(i), end=' ')



