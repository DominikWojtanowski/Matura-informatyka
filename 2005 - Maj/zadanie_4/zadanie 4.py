import math

def wylicz_mnoznik(n: int, option: int) -> float:
    return 0.01 * n if option == 1 else 0.5 * math.sqrt(n)

def obliczenia_programu(n: int, option: int) -> float:
    m = 0.0001 * n
    wynik = 10 * pow(m,3) + 7 * pow(m,2) + 0.1 * m + 0.1
    return wynik if option == 1 else wynik * 5

def calkowity_koszt(n : int, option: int) -> float:
    return wylicz_mnoznik(n,option) + obliczenia_programu(n,option)

koszty_lepsze_dla_D1 = []
koszty_lepsze_dla_D2 = []

with open("raport.txt","w") as f:
    pass

for N in range(1,7001):
    D1 = calkowity_koszt(N,1)
    D2 = calkowity_koszt(N,2)
    # print(D1, D2)
    if D1 < D2:
        koszty_lepsze_dla_D1.append(N)
        # f.write(f"dla N = {N} lepsze jest D1\n")
    else:
        koszty_lepsze_dla_D2.append(N)

        # f.write(f"dla N = {N} lepsze jest D2\n")

with open("raport.txt","a+") as f:
    f.write(f"Lepsze koszty dla D1: [{koszty_lepsze_dla_D1[0]},{koszty_lepsze_dla_D1[-1]}]\n" )
    f.write(f"Lepsze koszty dla D2: [{koszty_lepsze_dla_D2[0]},{koszty_lepsze_dla_D2[-1]}]\n" )

for N in [100,1000,5000]:
    with open("raport.txt","a+") as f:
        f.write(f"Koszt dla N = {N}, D1: {calkowity_koszt(N,1):.2f}\n")
        f.write(f"Koszt dla N = {N}, D2: {calkowity_koszt(N,2):.2f}\n\n")

with open("raport.txt", "a+") as f:
    f.write(f"podpunkt b: \n")
    for N in range(6000, 9100, 100):
        f.write(f"{N}, {wylicz_mnoznik(N,2):.2f}, {obliczenia_programu(N,2):.2f}\n")
