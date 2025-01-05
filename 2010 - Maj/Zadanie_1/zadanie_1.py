import math

str = "ALGORYTM_PRZESTAWIENIOWY"


str2 = "BTLLTU_ĘL_EOYPM_ĄPJZLCYNDREOKYLI_ZMFO_ĄGJY_Ó_N_DEWFWGISYSII_ŁEI_"
tab_length = math.ceil(math.sqrt(str2.__len__()))

print(tab_length)

szyfrArr = []

for i in range(str2.__len__() // tab_length):
    new_tab = list(str2[i * tab_length: (i + 1) * tab_length])
    szyfrArr.append(new_tab)

newArr = list(str2[str2.__len__() // tab_length * tab_length:])
if str2.__len__() % tab_length != 0:
    for i in range((tab_length - str2.__len__() % tab_length)):
        newArr.append('_')
if newArr != []:
    szyfrArr.append(newArr)

for i in szyfrArr:
    print(i)

for i in range(szyfrArr[0].__len__()):
    for j in range(szyfrArr.__len__()):
        print(' ' if szyfrArr[j][i] == "_" else szyfrArr[j][i], end='')
