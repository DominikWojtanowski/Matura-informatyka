from typing import List, Tuple


def calculate_lps(substr: str) -> List[int]:
    str_len = substr.__len__()

    lps = [0] * str_len

    i = 1
    j = 0

    while i < str_len:
        if substr[i] == substr[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1


    return lps

def kmp_search(main: str, sub: str) -> bool:
    sub_len = sub.__len__()
    main_len = main.__len__()

    # print(main)
    # print(sub)

    lps = calculate_lps(sub)

    i = 0
    j = 0

    while i < main_len:
        if main[i] == sub[j]:
            j += 1
            i += 1

            if j == sub_len:

                j = lps[j - 1]
                # wiecej nie jest mi potrzebne
                return True
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def printMatrix(main: str, main_len: int, sub: str, dp) -> None:
    print(end='    ')
    for idx in range(main_len):
        print(main[idx], end=' ')
    print()

    for (idx, lines) in enumerate(dp, start=0):
        if idx != 0:
            print(sub[idx - 1], sep=' ', end=' ')
        else:
            print(end='  ', sep=' ')
        for num in lines:
            print(str(num), sep=' ', end=' ')
        print()

def dpArr(main: str, sub: str) -> Tuple[int,int,int,str]:
    main_len = main.__len__()
    sub_len = sub.__len__()

    dp = [[0] * (main_len + 1) for _ in range(sub_len + 1)]


    # lenght, x, y
    max_tuple = (0,0,0,'')

    for i in range(main_len):
        for j in range(sub_len):
            if main[i] == sub[j]:
                dp[j + 1][i + 1] = dp[j][i] + 1

    for (idx, values) in enumerate(dp[-1]):
        if values - idx >= 0 and values != 0:
            if values > max_tuple[0]:
                max_tuple = (values, values, dp.__len__(), 'przod')
                string = 'przod'
    for (idx, value) in enumerate(dp[1:]):
        if value[-1] - idx > 0 and value[-1] != 0:
            if value[-1] > max_tuple[0]:
                max_tuple = (value[-1], dp[0].__len__() - 1, idx + 1, 'tyl')
                string = 'tyl'

    # for (idx, list) in enumerate(dp, start=0):
    #     for (v_idx, value) in enumerate(list, start=0):
    #         # print(v_idx)
    #         if v_idx - value < 1 and value != 0:
    #             if max_tuple[0] < value:
    #                 max_tuple = (value, v_idx - 1, idx - 1)
    #         if v_idx == dp[0].__len__() - 1 and value != 0:
    #             if max_tuple[0] < value:
    #                 max_tuple = (value, v_idx - 1, idx - 1)
    # if max_tuple[0] == 0:
    #     printMatrix(main,main_len,sub,dp)
    #     print()
    # printMatrix(main,main_len,sub,dp)





    return max_tuple

def isPalindrom(w: str) -> bool:
    mid = w.__len__() // 2
    for i in range(mid):
        if w[i] != w[-i - 1]:
            return False
    return True

with open("dane.txt", "r+") as file:
    with open("slowa.txt", "w+") as file2:
        palindromCount = 0
        wlaczneCount = 0
        brakCount = 0

        lines = file.readlines()
        for line in lines:
            line = line[:-1]

            lineArr = line.split(" ")
            for oneLine in lineArr:
                palindromCount += int(isPalindrom(oneLine))

            res = dpArr(lineArr[0],lineArr[1])
            if kmp_search(lineArr[0], lineArr[1]) == True:
                wlaczneCount += 1
                file2.write(f"{lineArr[0]}\n")
            elif res[0] == 0:
                brakCount += 1
                file2.write(f"{lineArr[1]}{lineArr[0]}")
            else:
                if res[-1] == 'tyl':
                    file2.write(f"{lineArr[0]}{lineArr[1][res[0]:]}\n")
                else:
                    file2.write(f"{lineArr[1][0:lineArr[1].__len__() - res[0]]}{lineArr[0]}\n")






    print(palindromCount)
    print(wlaczneCount)
    print(brakCount)


str_1 = "10011101"
str_2 = "1100"
result = dpArr(str_1, str_2)
if result[-1] == 'tyl':
    print(str_2[result[0]:])
else:
    print(str_2[0:str_2.__len__() - result[0]])
# 0100101 101110
print(result)
# wspolna_czesc = str_1[result[1] - result[0] + 1:result[1] + 1]
# wspolna_czesc_len = wspolna_czesc.__len__()
# # print(wspolna_czesc, wspolna_czesc_len)
# # print(str_2[0:result[0] - result[2] + 1])
# # print(result[1] - result[0] + 1)
# wkleic_z_przodu = str_2[:result[0] - result[2] + 1]
# wkleic_z_tylu = str_2[result[2] + 1:]

# poczatkowy_index = result[1] - result[0] + 1
# koncowy_index = result[1]

# print(poczatkowy_index, koncowy_index)





