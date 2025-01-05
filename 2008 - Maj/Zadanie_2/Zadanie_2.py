A = ['a','b'] # ??

w1: str = ''
w2: str = ''

w1w2: str = w1 + w2

def REG2(w: str) -> str:
    # print(w)
    if w.__len__() == 1:
        return "TAK"
    elif w.__len__() > 1 and w.__len__() % 2 == 1:
        return "NIE"
    elif w.__len__() > 1 and w.__len__() % 2 == 0:
        mid_len = w.__len__() // 2
        w1 = w[:mid_len]
        w2 = w[mid_len:]

        if w1 != w2:
            return "NIE"
        else:
            return REG2(w1)
        # print(w1,w2)
        # print(w1.__len__(), w2.__len__())

def REG3(w: str) -> str:
    if w.__len__() == 1:
        return "TAK"
    elif w.__len__() > 1 and w.__len__() % 3 != 0:
        return  "NIE"
    elif w.__len__() > 1 and w.__len__() % 3 == 0:
        onePart = w.__len__() // 3

        w1 = w[:onePart]
        x = w[onePart:onePart*2]
        w2 = w[onePart*2:]

        if w1 != w2 and w1 != x:
            return "NIE"
        else:
            return REG3(w1)

# for i in range(1,65):
#     print(REG2("a" * (2 ** i)))

print(REG3("aaaabaaba"))

