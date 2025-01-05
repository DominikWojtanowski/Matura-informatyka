from typing import List, Tuple

def schodyITP(arr: List[int]) -> List[Tuple[List[int], int, int]]:
    res: List[Tuple[List[int], int, int]] = []

    schody_list: List[int] = []
    dlugosc_schodow = 0
    ilosc_progow = 0

    isInProgress = False

    for idx in range(0, arr.__len__() - 1):
        if arr[idx] >= arr[idx + 1]:
            if arr[idx] != arr[idx + 1]:
                ilosc_progow += 1
            schody_list.append(arr[idx])
            dlugosc_schodow += 1
            isInProgress = True

        else:
            schody_list.append(arr[idx])
            new_list = schody_list.copy()
            if isInProgress:
                res.append((new_list,dlugosc_schodow + 1,ilosc_progow))
            dlugosc_schodow = 0
            ilosc_progow = 0

            schody_list.clear()

            isInProgress = False

    if isInProgress:
        schody_list.append(arr[-1])
    new_list = schody_list.copy()
    if isInProgress:
        res.append((new_list,dlugosc_schodow + 1,ilosc_progow))
    return res

def schodyZadanie(n: int, arr: List[int]) -> int:
    liczba_progow = 0
    for i in range(1,n):
        if arr[i - 1] > arr[i]:
            liczba_progow += 1
    return liczba_progow

def schodyZadanieC(n: int, arr: List[int]) -> int:
    najwieksza_liczba_progow = 0
    liczba_progow_curr = 0
    for i in range(1,n):
        if arr[i - 1] >= arr[i]:
            if arr[i - 1] > arr[i]:
                liczba_progow_curr += 1
        else:
            najwieksza_liczba_progow = liczba_progow_curr if liczba_progow_curr > najwieksza_liczba_progow else najwieksza_liczba_progow
            liczba_progow_curr = 0
    return najwieksza_liczba_progow

# print(schodyITP([3, 7, 7, 6, 5, 4, 4, 4, 5]))
# for oneTuple in schodyITP([2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]):
#     print(f'Schody: {oneTuple[0]}, dlugosc schodow: {oneTuple[1]}, ilosc progow: {oneTuple[2]}')

# liczba_wszystkich_progow = 0
print(schodyZadanie(9,[3, 7, 7, 6, 5, 4, 4, 4, 5]))
print(schodyZadanieC(9, [3, 7, 7, 6, 5, 4, 4, 4, 5]))
print(schodyZadanieC(20,[2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]))