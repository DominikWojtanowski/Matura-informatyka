import random
from typing import List

wystapienia_dict = dict({})

def sumEvenNumbersIsMoreThan42(n: str) -> bool:
    one_digit = 0
    sum = 0
    n = n[:-1]

    for i in n[::-1]:
        one_digit = ord(i) - ord('0')
        if one_digit % 2 == 0:
            sum += one_digit

    if sum > 42:
        return True
    return False

def minimumFourOnes(n: str) -> bool:
    ones = 0
    for i in n:
        if i == '1':
            ones += 1
            if ones == 4:
                return True
    return False


def swap_variables(arr, idx1, idx2):
    tmp = arr[idx1]

    arr[idx1] = arr[idx2]
    arr[idx2] = tmp

def partition(arr: List[str], low: int, high: int):
    random_idx = random.randint(low, high)
    random_pivot = arr[random_idx]

    swap_variables(arr, high, random_idx)

    i = low - 1
    for j in range(low, high):
        if arr[j] <= random_pivot:
            i += 1
            swap_variables(arr, j, i)
    swap_variables(arr, high, i + 1)

    return i + 1



def quickSort(arr: List[str], low: int , high: int) -> List[str]:
    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr


def lastTwoMedianDividalbleWithThree(n: str) -> bool:
    n = n[:-1]
    if n[-1] == '2':
        n = quickSort(list([i for i in n]),0,n.__len__()-1)
        if n.__len__() % 2 == 1:
            return (ord(n[n.__len__() // 2]) - ord('0')) % 3 == 0
        else:
            return ((ord(n[n.__len__() // 2]) - ord('0')) + (ord(n[n.__len__() // 2 - 1]) - ord('0'))) % 3 == 0
    return False


with open("zadanie_6.txt","r+") as file:
    lines = file.readlines()

    sum = 0
    for line in lines:
        if sumEvenNumbersIsMoreThan42(line):
            sum += 1
    print(sum)

with open("zadanie_6.txt","r+") as file:
    lines = file.readlines()

    sum = 0
    for line in lines:
        if minimumFourOnes(line):
            sum += 1
    print(sum)

with open("zadanie_6.txt","r+") as file:
    lines = file.readlines()

    sum = 0
    for line in lines:
        if lastTwoMedianDividalbleWithThree(line):
            sum += 1
    print(sum)


with open("zadanie_6.txt","r+") as file:
    lines = file.readlines()

    sum = 0
    for line in lines:
        line = line[:-1]
        if line not in wystapienia_dict:
            wystapienia_dict[line] = 1
            sum += 1
        else:
            wystapienia_dict[line] += 1
    for key, item in wystapienia_dict.items():
        if item >= 2:
            print(f"{key}: {item}")

    print(wystapienia_dict)