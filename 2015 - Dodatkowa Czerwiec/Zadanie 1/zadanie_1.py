def notFun(x: str) -> str:
    return '0' if x == '1' else '1'

def u2(n: int, a: str) -> str:
    i = 0
    j = 1
    b = ['0'] * a.__len__()

    a = a[::-1]
    while i < n - 1 and a[i] == '0':
        b[i] = '0'
        i += 1

    b[i] = a[i]
    i += 1
    while i < n:
        print(j)
        b[i] = notFun(a[i])
        i += 1
        j += 1
    return ''.join(b[::-1])

# print(u2(16,'1111001001110000'))
# print(u2(16,'0000000000000000'))
print(u2(16,'1111111100000000'))