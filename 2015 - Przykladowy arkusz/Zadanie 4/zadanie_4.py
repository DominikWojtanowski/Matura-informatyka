def isNumberAnagram(a: str, b: str) -> bool:
    numbersADict = dict()
    numbersBDict = dict()

    for (idx, i) in enumerate(a):
        if a[idx] in numbersADict:
            numbersADict[a[idx]] += 1
        else:
            numbersADict[a[idx]] = 1

        if b[idx] in numbersBDict:
            numbersBDict[b[idx]] += 1
        else:
            numbersBDict[b[idx]] = 1

    return numbersBDict == numbersADict

def createLargestAnagram(n: str) -> str:
    n_len = n.__len__()
    n_list = [i for i in n]
    for i in range(0,n_len):
        for j in range(1, n_len - i):
            if n_list[j] > n_list[j - 1]:
                tmp = n_list[j]
                n_list[j] = n_list[j - 1]
                n_list[j - 1] = tmp

    return "".join(n_list)

with open('dane_anagramy.txt','r+') as file:
    numberAnagrams = 0
    maxAnagrams = 0
    currAnagrams = 0

    lines = file.readlines()

    anagram_dict = dict()



    for line in lines:
        lineArr = line.split(' ')
        if lineArr[1][-1] == '\n':
            lineArr[1] = lineArr[1][:-1]

        if isNumberAnagram(lineArr[0],lineArr[1]):
            numberAnagrams += 1

        anagram_uno = createLargestAnagram(lineArr[0])
        anagram_dos = createLargestAnagram(lineArr[1])

        if anagram_dos in anagram_dict:
            anagram_dict[anagram_dos] += 1
        else:
            anagram_dict[anagram_dos] = 1

        if anagram_uno in anagram_dict:
            anagram_dict[anagram_uno] += 1
        else:
            anagram_dict[anagram_uno] = 1



    print(numberAnagrams)
    print(maxAnagrams)
    for key, item in anagram_dict.items():
        if maxAnagrams < item:
            maxAnagrams = item

    print(maxAnagrams)
print(createLargestAnagram('293211'))