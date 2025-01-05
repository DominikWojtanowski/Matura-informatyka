from typing import List, Tuple

def isBigger(hour1: str, hour2: str):
    l1 = hour1.split(':')
    l2 = hour2.split(':')
    time1 = int(l1[0]) *  60 + int(l1[1])
    time2 = int(l2[0]) * 60 + int(l2[1])

    return time1 > time2


def isBiggerOrEqual(hour1: str, hour2: str):
    l1 = hour1.split(':')
    l2 = hour2.split(':')
    time1 = int(l1[0]) * 60 + int(l1[1])
    time2 = int(l2[0]) * 60 + int(l2[1])

    return time1 >= time2

def isSmallerOrEqual(hour1: str, hour2: str):
    l1 = hour1.split(':')
    l2 = hour2.split(':')
    time1 = int(l1[0]) * 60 + int(l1[1])
    time2 = int(l2[0]) * 60 + int(l2[1])

    return time1 <= time2

def isSmaller(hour1: str, hour2: str):
    l1 = hour1.split(':')
    l2 = hour2.split(':')
    time1 = int(l1[0]) * 60 + int(l1[1])
    time2 = int(l2[0]) * 60 + int(l2[1])

    return time1 < time2


def bubbleSort2(T: List[Tuple[int,str,str,int]], idxSort: int, reverseBool: bool, additionalIf: int):

    strategy = idxSort - 1
    if type(T[0][strategy]) == str:
        for i in range(T.__len__() - 1):
            for j in range(T.__len__() - 1 - i):
                if isBigger(T[j][strategy],T[j + 1][strategy]) if (not reverseBool) else isSmaller(T[j][strategy],T[j + 1][strategy]):
                    tmp = T[j]
                    T[j] = T[j + 1]
                    T[j + 1] = tmp
                else:
                    if T[j][strategy] == T[j + 1][strategy] and isSmaller(T[j + 1][2],T[j][2]) if additionalIf == 2 else isBigger(T[j + 1][1], T[j][1]):
                        tmp = T[j]
                        T[j] = T[j + 1]
                        T[j + 1] = tmp

    else:
        for i in range(T.__len__() - 1):
            for j in range(T.__len__() - 1 - i):
                if T[j][strategy] > T[j + 1][strategy] if (not reverseBool) else T[j][strategy] < T[j + 1][strategy]:
                    tmp = T[j]
                    T[j] = T[j + 1]
                    T[j + 1] = tmp

    return T


def fun(T: List[Tuple[int,str,str,int]], S, reverse, startLateOrEndEarly: int):
    P = []

    S += 1
    T = bubbleSort2(T, S, reverse, startLateOrEndEarly)

    j = 0
    while T.__len__() != 0:
        x = T[0]
        T = T[1:]

        P.append(x)

        do_usuniecia = []
        for i in T:
            if isBiggerOrEqual(i[1],x[1]) and isSmaller(i[1],x[2]):
                do_usuniecia.append(i)
            if isSmallerOrEqual(i[1],x[1]) and isBiggerOrEqual(i[2],x[1]):
                do_usuniecia.append(i)

        for i in do_usuniecia:
            T.remove(i)

        j += 1

    return P

T = [(1,"9:00","12:00",3),(2,"15:00","17:00",2),(3, "11:00", "16:00",5),(4,"12:00","14:00",2),(5,"11:30","12:30",1)]

print(fun(T,3, True, 2))
print(fun(T,3, False, 2))
print(fun(T,1,False,2))
print(fun(T,2,False,2))

