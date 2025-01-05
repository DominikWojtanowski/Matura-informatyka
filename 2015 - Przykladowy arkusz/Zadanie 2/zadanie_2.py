def f(n: int):
    k = 1
    ilosc_sprawdzen = 0
    while ((k + 1) * (k + 1)) <= n:
        ilosc_sprawdzen += 1
        k += 1
    print(ilosc_sprawdzen)
    return k

def f2(n: int) -> int:
    k = 1
    m = n
    ilosc_porownan = 0
    while (k + 1) * (k + 1) <= n:
        s = (k + m) // 2
        if s * s <= n:
            k = s
        else:
            m = s
        ilosc_porownan += 2
    print(ilosc_porownan)
    return k

print(f(32))