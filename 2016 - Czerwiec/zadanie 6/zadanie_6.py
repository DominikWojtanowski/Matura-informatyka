def baseOtherToBaseTen(num, fromBase):
    res = 0

    for idx, i in enumerate(num[::-1]):
        res += int(i) * fromBase ** idx
    return res

def checkBaseFour(num):
    for i in num:
        if i == '0':
            return False
    return True

with open('liczby.txt','r+') as file:
    lines = [line.strip() for line in file.readlines()]

    min = 9999999999
    minNum = "0"
    max = -9999999999
    maxNum = "0"
    octNumCount = 0
    octSum = 0
    baseFourNumCount = 0
    binaryEvenNumCount = 0



    for line in lines:
        if min > baseOtherToBaseTen(line[:-1], int(line[-1])):
            min = baseOtherToBaseTen(line[:-1], int(line[-1]))
            minNum = line
        if max < baseOtherToBaseTen(line[:-1], int(line[-1])):
            max = baseOtherToBaseTen(line[:-1], int(line[-1]))
            maxNum = line
        if line[-1] == '8':
            octNumCount += 1
            octSum += baseOtherToBaseTen(line[:-1],8)
        if line[-1] == '4':
            if checkBaseFour(line[:-1]):
                baseFourNumCount += 1
        if line[-1] == '2':
            if baseOtherToBaseTen(line[:-1],2) % 2 == 0:
                binaryEvenNumCount += 1

    with open('wyniki_6_1.txt', 'w') as writeOne:
        writeOne.write(f"{octNumCount}\n")
    with open('wyniki_6_2.txt','w') as writeSecond:
        writeSecond.write(f"{baseFourNumCount}\n")
    with open('wyniki_6_3.txt','w') as writeThird:
        writeThird.write(f"{binaryEvenNumCount}\n")
    with open('wyniki_6_4.txt','w') as writeFourth:
        writeFourth.write(f"{octSum}")
    with open('wyniki_6_5.txt','w') as writeFifth:
        writeFifth.write(f"{minNum}, {min}\n{maxNum}, {max}")
