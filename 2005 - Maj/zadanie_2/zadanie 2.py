from typing import Tuple
from math import log2

reguly_dict = {"A": ["BC","CD"],
               "B": ["AD"],
               "C": ["BA"],
               "D": ["AA","BB"]}

organism = "ADBA"
tmp_organism = ""
organism_list = []
tmp_organism_list = []

def all_variations(organism: str) -> list:
    organism_list = []
    tmp_organism_list = []
    tmp_organism = ""
    for idx, letter in enumerate(organism, start=0):
        tmp_organism = ""
        if len(reguly_dict[letter]) > 1:
            if len(organism_list) == 0:
                for letter_seq in reguly_dict[letter]:
                    organism_list.append(letter_seq)
            else:
                for seq in organism_list:
                    for new_seq in reguly_dict[letter]:
                        tmp_organism_list.append(seq + new_seq)
                organism_list.clear()
                for new_letter_seq in tmp_organism_list:
                    organism_list.append(new_letter_seq)
                tmp_organism_list.clear()
        else:
            organism_list = [i + reguly_dict[letter][0] for i in organism_list]
    return organism_list
# text = "\n".join(all_variations(organism))
# print(f'Mozliwe wariacje: \n{organism}')

def checkIfPowerOfTwo(natual_number: int) -> Tuple[bool, int]:
    age = 1
    if natual_number > 0 and natual_number & (natual_number - 1) == 0:
        while not (natual_number == 1):
            age += 1
            natual_number = natual_number // 2
        return (True, age)
    return (False, 0)

    # bitowo powiedzmy ze 64 to 10000000 a 63 to 01111111 kazda potega ma tylko jeden bit
    # ktory jest jedynka a liczba o 1 od niego mniejsza ma wszystkie inne bity jako jedynki, wiec andowanie zawsze da 0
def checkIfCanExist(natural_number: int) -> Tuple[bool, int]:
    if natural_number == 1 or checkIfPowerOfTwo(natual_number=natural_number)[0] == True:
        return (True, checkIfPowerOfTwo(natual_number=natural_number)[1])
    return (False, 0)

def trueLengthCount(n: int, m: int) -> int:
    count = 0
    starting_pow = 0
    power_of_two_value = 0
    if(checkIfPowerOfTwo(n)[0] == True):
        starting_pow = int(log2(n))
    else:
        starting_pow = int(log2(n + 1))

    power_of_two_value = 2 ** starting_pow

    if power_of_two_value <= n:
        power_of_two_value *= 2

    while power_of_two_value <= m:
        power_of_two_value *= 2
        count += 1

    print(count)


# print(checkIfCanExist(1))
# print(checkIfCanExist(2))
# print(checkIfCanExist(3))
# print(checkIfCanExist(10))
# print(checkIfCanExist(8))
print(trueLengthCount(7,33))

def sprawdz(napis: str, start: str) -> str:
    napis_1 = ""
    napis_2 = ""
    if checkIfPowerOfTwo(len(napis))[0] == False:
        return "NIE"
    else:
        if napis == start:
            return "TAK"
        if len(napis) == 1:
            return "NIE"

        napis_1, napis_2 = napis[int(len(napis)/2):], napis[:int(len(napis)/2)]
        for idx in range(len(napis)):
            if(napis[idx] == start):
                wynik_1 = sprawdz(napis_1,reguly_dict[napis[idx]][0])
                wynik_2 = sprawdz(napis_2,reguly_dict[napis[idx]][1])
                if wynik_1 == "TAK" and wynik_2 == "TAK":
                    return "TAK"
        return "NIE"
print(sprawdz("BCAAADCD","A"))