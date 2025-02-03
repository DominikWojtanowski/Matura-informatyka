def isTwoCyclic(num):
    if len(num) % 2 != 0:
        return False
    else:
        return num[:len(num)//2] == num[len(num)//2:]

def binToTen(num):
    res = 0
    for (idx, i) in enumerate(num[::-1]):
        res += (ord(i) - ord('0')) * 2 ** idx
    return res

def isCorrect(num: str):
    for i in range(0,len(num),4):
        if binToTen(num[i:i+4]) > 9:
            return False
    return True

with open('binarne.txt','r+') as file:
    lines = [line.strip() for line in file.readlines()]

    isTwoCyclicCount = 0
    maxTwoCyclicLen = -1
    maxTwoCyclicBin = ""
    isInCorrectCount = 0
    minLen = 9999999
    maxLen = -2320983092830
    minBin = ""
    maxBin = ""
    for line in lines:
        if isTwoCyclic(line):
            isTwoCyclicCount += 1
            if len(line) > maxTwoCyclicLen:
                maxTwoCyclicLen = len(line)
                maxTwoCyclicBin = line
        if not isCorrect(line):
            if line.__len__() < minLen:
                minLen = line.__len__()
                minBin = line
            isInCorrectCount += 1
        if binToTen(line) <= 65535:
            if binToTen(line) > maxLen:
                maxLen = binToTen(line)
                maxBin = line

    print(isTwoCyclicCount, maxTwoCyclicLen, maxTwoCyclicBin)
    print(isInCorrectCount, minLen, minBin)
    print(maxBin, maxLen)

