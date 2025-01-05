system_szesnastkowy = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
liczba_wystapien = dict({})


parzyste = 0

palindroms = 0



with open("dane.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        isPalindrom = True
        idx = 0
        liczba = 0
        line = line[:-1]
        for letter in line[::-1]:

            liczba += system_szesnastkowy[letter.upper()] * 16 ** idx
            idx += 1

        for i in range(len(line)):

            if line[i] != line[-(i + 1)]:
                isPalindrom = False
                break

        if line not in liczba_wystapien:
            liczba_wystapien[line] = 1
        else:
            liczba_wystapien[line] += 1

        if liczba % 2 == 0:
            parzyste += 1

        if isPalindrom == True:
            palindroms += 1




# print(liczba_wystapien)
max_value = 0
max_key = ""
for key, item in liczba_wystapien.items():
    if item > max_value:
        max_key = key
        max_value = item

print(max_value, max_key)

print(parzyste)
print(palindroms)