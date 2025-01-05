from typing import Tuple, List

def znajdzOdpowiedniaIlosc(liczba: int) -> Tuple[int, int]:
    i = 1
    odpowiedniaSuma = 0
    while liczba > 0:
        liczba -= i
        odpowiedniaSuma += i
        i += 1

    return (odpowiedniaSuma, i-1)

def stworzTablicePascala(tab: List[int], wysokosc: int) -> List[List[int]]:
    tabLen = tab.__len__()

    newTab = []

    poczatek = 0
    koniec = 0

    for i in range(1, wysokosc + 1):
        przedzial = tab[poczatek: koniec + i]
        koniec += i
        poczatek += i
        newTab.append(przedzial)


    przedzialGoraPoczatek = 2
    przedzialLewyPoczatek = 1

    for (idx,i) in enumerate(range(przedzialGoraPoczatek, wysokosc), start=1):
        for j in range(przedzialLewyPoczatek, i):
            newTab[i][j] = newTab[i-1][j-1] + newTab[i-1][j]

    return newTab

def wyszukajMaxZTab(tab):
    return tab[len(tab)//2]

def znajdzSumeCyfrWLiczbie(liczba: int) -> int:
    i = 0
    while liczba > 0:
        liczba //= 10
        i += 1
    return i

def znajdzLiczbeCyfr(tab: List[List[int]]) -> List[Tuple[int,int]]:
    sumaCyfr = 0
    listaTupli = []

    for (idx,oneTab) in enumerate(tab, start=1):
        sumaCyfr = 0
        for oneValue in oneTab:
            sumaCyfr += znajdzSumeCyfrWLiczbie(oneValue)
        newTupla = (idx,sumaCyfr)
        listaTupli.append(newTupla)

    return listaTupli

def znajdzLiczbeWierzzyGdzieLiczbaNieJestPodzielnaPrzezPiec(tab: List[List[int]]) -> List[int]:
    numeryWierszy = []

    for (idx, oneTab) in enumerate(tab, start=1):
        warunek = True
        for oneValue in oneTab:
            if oneValue % 5 == 0:
                warunek = False
                break
        if warunek:
            numeryWierszy.append(idx)

    return numeryWierszy

def rownoRamiennyTrojkat(tablicaPascala: List[List[int]]):
    maxIloscSpacji = tablicaPascala.__len__()
    for (idx, oneTab) in enumerate(tablicaPascala, start=1):
        print(' ' * (maxIloscSpacji - idx), end='')
        for oneValue in oneTab:
            print(oneValue, end=' ')
        print()

def prostokatnyTrojkatSierpinskiego(tablicaPascala: List[List[int]]):
    for oneList in tablicaPascala:
        for oneValue in oneList:
            print(f"{'X' if oneValue % 3 == 0 else ' '}",end='')
        print()

def rownoRamiennyTrojkatSierpinskiego(tablicaPascala: List[List[int]]):
    maxIloscSpacji = tablicaPascala.__len__()
    for (idx, oneTab) in enumerate(tablicaPascala, start=1):
        print(' ' * (maxIloscSpacji - idx), end='')
        for oneValue in oneTab:
            print(f"{'X' if oneValue % 3 == 0 else ' '}", end=' ')
        print()

sum = 0
for i in range(1,31):
    sum += i

daneTablicy = znajdzOdpowiedniaIlosc(sum)
nieWypelnionaTablicaPascala = [1] * daneTablicy[0]
print(nieWypelnionaTablicaPascala.__len__())

wypelnionaTablicaPascala = stworzTablicePascala(nieWypelnionaTablicaPascala, daneTablicy[1])

print(wyszukajMaxZTab(wypelnionaTablicaPascala[9]))
print(wyszukajMaxZTab(wypelnionaTablicaPascala[19]))
print(wyszukajMaxZTab(wypelnionaTablicaPascala[29]))
# print(wypelnionaTablicaPascala[19])

for tupleValue in znajdzLiczbeCyfr(wypelnionaTablicaPascala):
    print(tupleValue)

# print(wypelnionaTablicaPascala)
print(znajdzLiczbeWierzzyGdzieLiczbaNieJestPodzielnaPrzezPiec(wypelnionaTablicaPascala))
prostokatnyTrojkatSierpinskiego(wypelnionaTablicaPascala)
rownoRamiennyTrojkatSierpinskiego(wypelnionaTablicaPascala)

# testowaIlosc = 21
# testoweDaneTablicy = znajdzOdpowiedniaIlosc(testowaIlosc)
# nieWypelnionaTestowaTablica = [1] * testoweDaneTablicy[0]
#
# wypelnionaTestowaTablica = stworzTablicePascala(nieWypelnionaTestowaTablica, testoweDaneTablicy[1])
# rownoRamiennyTrojkat(wypelnionaTestowaTablica)

