def EvenIsGreater(liczbaNieParzysta, liczbaParzysta):
    return True
def BothEvenIsGreater(liczbaParzysta, innaLiczbaParzysta):
    return liczbaParzysta > innaLiczbaParzysta
def BothOddIsGreater(liczbaNieParzysta, innaLiczbaNieParzysta):
    return liczbaNieParzysta < innaLiczbaNieParzysta

def greater(a, b):
    return a > b

def sortowanie(arr, fun):
    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr) - 1):
            if fun(arr[i], arr[j + 1]):
                tmp = arr[j+1]
                arr[j+1] = arr[i]
                arr[i] = tmp
    return arr

def sortujTablice(arr):
    arrEven = []
    arrOdd = []

    for i in arr:
        arrEven.append(i) if i % 2 == 0 else arrOdd.append(i)

    sortedArrEven = sortowanie(arrEven, BothEvenIsGreater)
    sortedArrOdd = sortowanie(arrOdd, BothOddIsGreater)


    return sortedArrEven + sortedArrOdd

print(sortujTablice([3, 6, 8, 11, 15, 20, 35, 70, 100, 1000])) # 2.1
print(sortujTablice([27,16,7,32,10,12])) # 2.2
