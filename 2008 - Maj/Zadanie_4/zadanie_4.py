from typing import Dict, List

def dHondta(v: int, s: int) -> int:
    return v // (s + 1)

def glosyKazdyZKomitetow(komitety: Dict[str,int], ilosc_mandatow: int):
    res_dict = {}
    X_multipliers = []

    for key in komitety.keys():
        res_dict[key] = 0

    # print(res_dict)

    for i in range(ilosc_mandatow):
        X_multipliers.clear()
        for key in komitety.keys():
            X_multipliers.append(dHondta(komitety[key],res_dict[key]))

        max_idx = 0
        max_value = 0
        for (idx,j) in enumerate(X_multipliers,start=0):
            if j > max_value:
                max_value = j
                max_idx = idx

        res_dict[chr(ord('A') + max_idx)] += 1

    return  res_dict

komitety_dict = {}
komitety_zdobyte_glosy = {}

glosy_arr = []
laczna_ilosc_mandatow: Dict[str, int] = dict({})
laczna_ilosc_glosow: Dict[str, int] = dict({})

najmniejszaIlosc = [1000000,100000]
najwiekszaIlosc = [0,0]

# print(ord('A'))

with open("dane.txt", "r+") as file:
    lines = file.readlines()
    line = lines[0][:-1]

    tmp = line.split(" ")[:-1]
    for (idx, i) in enumerate(tmp):
        laczna_ilosc_mandatow[chr(ord('A') + idx)] = 0
        laczna_ilosc_glosow[chr(ord('A') + idx)] = 0

    for (idx, line) in enumerate(lines, start=1):
        line = line[:-1]
        line_to_list = line.split(" ")

        items = 0
        for item in line_to_list[:-1]:
            items += int(item)

        if items > najwiekszaIlosc[1]:
            najwiekszaIlosc[0] = idx
            najwiekszaIlosc[1] = items
        elif items < najmniejszaIlosc[1]:
            najmniejszaIlosc[0] = idx
            najmniejszaIlosc[1] = items


        for (idx, i) in enumerate(line_to_list[:-1], start=0):
            komitety_dict[chr(65 + idx)] = int(i)
            laczna_ilosc_glosow[chr(65 + idx)] += int(i)

        numer_mandatow = int(line_to_list[-1])
        komitety_zdobyte_glosy = glosyKazdyZKomitetow(komitety_dict, numer_mandatow)

        glosy_arr.append(komitety_zdobyte_glosy)

    for zdobyte_glosy in glosy_arr:
        for (key, item) in zdobyte_glosy.items():
            laczna_ilosc_mandatow[key] += item

    print(laczna_ilosc_glosow)
    print(laczna_ilosc_mandatow)
    print(najwiekszaIlosc, najmniejszaIlosc)
    print(glosy_arr[5])




