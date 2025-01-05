from typing import List, Dict
def checkIfSameLenght(lines, len):
    for oneLine in lines:
        if oneLine.__len__() != len:
            return False
    return True

def checkIfAnagram(firstLine, lines):
    firstSet = set(firstLine)

    for line in lines:
        if firstSet != set(line):
            return False

    dictArr: List[Dict[str, int]] = []

    for line in lines:
        new_dict = dict()
        for letter in line:
            if letter in new_dict:
                new_dict[letter] += 1
            else:
                new_dict[letter] = 1
        dictArr.append(new_dict)

    for unoDict in dictArr:
        if unoDict != dictArr[0]:
            return False
    return True

with open('anagram.txt', 'r+') as file:
    with open('odp_4a.txt', 'w+') as writeToFile:
        with open('odp_4b.txt', 'w+') as writeToFileTwo:
            lines = file.readlines()
            for line in lines:
                zapisz = True
                line = line[:-1]

                linesTab = line.split(' ')
                lineLength = linesTab[0].__len__()

                if checkIfSameLenght(linesTab,lineLength):
                    writeToFile.write(f"{line}\n")
                    if checkIfAnagram(linesTab[0],linesTab):
                        writeToFileTwo.write(f"{line}\n")





