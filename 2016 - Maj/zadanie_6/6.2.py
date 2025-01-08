def odszyfrowanie(slowo, klucz):
    res = ""
    for litera in slowo:
        rundy = klucz % 26

        value = ord(litera) - rundy
        if value < ord('A'):
            value = ord('Z') - (64 - value)
        res += chr(value)
    return res


with open('dane_6_2.txt','r') as file:
    lines = [line.replace('\n','').split(' ')for line in file.readlines()]
    with open('wyniki_6_2.txt','w') as toWrite:
        for line, klucz in lines:
            print(klucz)
            toWrite.write(f"{odszyfrowanie(line,int(klucz))}\n")



