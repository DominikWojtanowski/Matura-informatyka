def convertToDecimal(num: str, orginalBase: int) -> int:
    res = 0

    for (idx,i) in enumerate(num[::-1]):
        res += int(i) * orginalBase ** idx

    return res


def hasMoreZeroesThanOnes(num: str) -> bool:
    res = dict()

    res['0'] = 0
    res['1'] = 0

    for letter in num:
        res[letter] += 1

    return res['0'] > res['1']



with open('liczby.txt', 'r+') as file:
    lines = file.readlines()

    moreZeroesThanOnes = 0
    dividableBy2 = 0
    dividableBy8 = 0

    maxBin = -10
    maxBinColumn = -1
    minBin = 2739871293797237129379812738971892738917298
    minBinColumn = -1
    for (i,line) in enumerate(lines,start=1):
        line = line[:-1]

        if hasMoreZeroesThanOnes(line):
            moreZeroesThanOnes += 1

        res = convertToDecimal(line,2)

        if res % 2 == 0:
            dividableBy2 += 1
        if res % 8 == 0:
            dividableBy8 += 1

        if res > maxBin:
            maxBin = res
            maxBinColumn = i
        if res < minBin:
            minBin = res
            minBinColumn = i


    print(moreZeroesThanOnes)
    print(dividableBy2)
    print(dividableBy8)
    print(maxBinColumn, minBinColumn)

