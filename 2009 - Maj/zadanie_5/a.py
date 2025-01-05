def najdluzszy_wspolny_fragment(a, b):
    n = len(a)
    m = len(b)

    # Tworzymy tablicę do dynamicznego programowania
    dp = [[0] * (m + 1)] * (n + 1)

    print(n,m)
    print(dp)
    najdluzszy = 0
    indeks_poczatkowy = -1

    # Przechodzimy przez oba ciągi i wypełniamy tablicę
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > najdluzszy:
                    najdluzszy = dp[i][j]
                    indeks_poczatkowy = i - najdluzszy  # Indeks początku fragmentu w a

    # Zwracamy najdłuższy fragment oraz jego indeks
    return a[indeks_poczatkowy:indeks_poczatkowy + najdluzszy], indeks_poczatkowy


# Przykład użycia
a = "10011101"
b = "1100"

najdluzszy_fragment, indeks_poczatkowy = najdluzszy_wspolny_fragment(a, b)
print(f"Najdłuższy fragment: '{najdluzszy_fragment}' zaczyna się na indeksie {indeks_poczatkowy}")
