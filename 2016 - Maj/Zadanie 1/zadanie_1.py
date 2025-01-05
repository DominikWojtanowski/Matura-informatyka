def sumaWszystkichRoznychDzielnikowLiczby(num):
    res = 0

    for i in range(1, num):
        if num % i == 0:
            res += i
            print(i, end=', ')
    print(end='\n')
    print(res)
    return res

def czySkojarzone(sumaDzielnikowA, A, sumaDzielnikowB, B):
    return ((B + 1) == sumaDzielnikowA) and ((A + 1) == sumaDzielnikowB)

a = 75
b = 48
sumaA = sumaWszystkichRoznychDzielnikowLiczby(a)
sumaB = sumaWszystkichRoznychDzielnikowLiczby(b)
print(czySkojarzone(sumaDzielnikowA=sumaA, sumaDzielnikowB=sumaB, A=a, B=b))