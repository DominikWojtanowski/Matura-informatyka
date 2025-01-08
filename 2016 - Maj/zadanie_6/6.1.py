def szyfrCezara(slowo, klucz):
    res = ""
    for litera in slowo:
        value = (ord(litera) + (klucz % (91 - 65)))
        if value > ord('Z'):
            value = value - ord('Z') + ord('A')
        res += chr(value)
    return res
klucz = 107

with open('dane_6_1.txt','r') as file:
    lines = [line.replace('\n','') for line in file.readlines()]
    with open('wyniki_6_1.txt','w') as toWrite:
        for line in lines:
            toWrite.write(f"{szyfrCezara(line,klucz)}\n")


