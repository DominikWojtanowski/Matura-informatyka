def f(n: int) -> int:
    wynik = 0
    while n != 0:
        wynik = wynik + (n % 10)
        print(wynik)
        n = n // 10
    return wynik

# print(f(36789))
# print(f(11111111))
print(f(1234))