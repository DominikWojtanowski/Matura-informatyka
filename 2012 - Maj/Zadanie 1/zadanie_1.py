def FRek(i, n, a, iloscPorownan):
    iloscPorownan += 1
    if i == n:
        return n
    else:
        j = FRek(i+1, n, a, iloscPorownan)
        print(f"a[{i}]: {a[i]} < a[{j}]: {a[j]}")
        if a[i] < a[j]:
            return i
        else:
            return j

def FIter(i,n,a):
    poczatek = i
    i = n - 2
    j = n - 1
    while i >= poczatek:
        print(f"a[{i}]: {a[i]} < a[{j}]: {a[j]}")
        if a[i] < a[j]:
            j = i
            i -= 1
        else:
            i -= 1
    return a[j]


a = [5,1,8,9,7,2,3,11,20,15,11,11]
iArr = [9,7,5]

# for i in iArr:
#     print(FRek(i, 10, a,0))
#
# print(a[FRek(5,10,a,0)])

iArr2 = [2,4,8]

FRek(4,11,a,0)
print('_' * 20)
print(FIter(4,11,a))




# a_mod = [0] * 2013
#
# print(FRek(512,2012,a_mod,0))



