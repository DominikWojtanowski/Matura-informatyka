from typing import List, Dict

tablica_wag = [1,3,7,9,1,3,7,9,1,3]
nieprawidlowe_numery_pesel = []
lata_arr = [0,0,0,0,0] # lata 50, 60, 70, 80, 90
lata_opis = ['lata_piecdziesiate','lata_szescdziesiate','lata_siedemdziesiate','lata_osiemdziesiate','lata_dziewiecdziesiate' ]

def checkIfGoodPesel(liczba: str) -> bool:
    sum = 0
    for (idx,letter) in enumerate(liczba[:-1]):
        sum += int(letter) * tablica_wag[idx]

    reszta = sum % 10
    ostatnia_liczba = 0 if reszta == 0 else 10 - reszta
    return str(liczba[-1]) == str(ostatnia_liczba)



def sortowanieBabelkowe(arr: List[str], kolejnosc: int):
    len = arr.__len__()

    for i in range(len):
        for j in range(0, len - i - 1):
            if arr[j + 1] > arr[j]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

    return arr

with open('pesel.txt', 'r+') as file:
    ile_osob_w_grudniu = 0
    ile_kobiet = 0
    rok_dict = dict()

    lines = file.readlines()
    for line in lines:
        line = line[:-1]

        if line[2:4] == '12':
            ile_osob_w_grudniu += 1
        if int(line[-2]) % 2 == 0:
            ile_kobiet += 1

        if f"19{line[0:2]}" in rok_dict:
            rok_dict[f"19{line[0:2]}"] += 1
        else:
            rok_dict[f"19{line[0:2]}"] = 1

        lata_arr[int(line[0:2]) // 10 - 5] += 1

        if checkIfGoodPesel(line) == False:
            nieprawidlowe_numery_pesel.append(line)

    max = -10
    rok = ''

    for key, item in rok_dict.items():
        if int(item) > max:
            max = int(item)
            rok = key

    print(ile_osob_w_grudniu)
    print(ile_kobiet)
    print(rok, max)
    print(sortowanieBabelkowe(nieprawidlowe_numery_pesel,0))

    for (idx,value) in enumerate(lata_arr):
        print(f"{lata_opis[idx]} {value/100}")

