def Ciag_Pentacciego(n): # kod do sprawdzenia, lepiej liczyc na kartce
    p_c = [0,1,1,2,4] # ,8

    if n < 5:
        return p_c[n]
    if n == 5:
        return 8
    else:
        p = 8
        for i in range(6,n+1):
            p_c.append(p)
            p = p + (p - p_c[i-6])
    return p


# 2.3

def CiagRn(n):
    poczatkowa_lista = [0,1,1,0,0,0,0]

    if n <= 6:
        return poczatkowa_lista[n]
    else:
        for i in range(7,n+1):
            poczatkowa_lista[0], poczatkowa_lista[1], poczatkowa_lista[2], poczatkowa_lista[3], poczatkowa_lista[4], poczatkowa_lista[5], poczatkowa_lista[6] = poczatkowa_lista[1], poczatkowa_lista[2], poczatkowa_lista[3], poczatkowa_lista[4], poczatkowa_lista[5], poczatkowa_lista[6], poczatkowa_lista[1]
    liczba = poczatkowa_lista[-1]
    return liczba


print([Ciag_Pentacciego(i) % 2 for i in range(15)])
print([CiagRn(i) for i in range(15)])

