def nwd(a,b,idx):
    idx += 1
    if b == 0:
        return (a, idx)
    else:
        return nwd(b, a % b, idx)

def zmodyfikowany_nwd(a,b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

# print(nwd(72,56,0)[1])
print(nwd(56,72,0)[0])
print(zmodyfikowany_nwd(56,72))
