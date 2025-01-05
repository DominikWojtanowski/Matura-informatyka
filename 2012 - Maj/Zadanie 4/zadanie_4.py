def szyfruj(napis: str, klucz: str):
    new_napis = ""
    dlugosc_klucza = klucz.__len__()
    for (idx, letter) in enumerate(napis):
        liczba_dodaj = ord(letter) + (ord(klucz[idx % dlugosc_klucza]) - ord('A') + 1)

        if liczba_dodaj > 90:
            liczba_dodaj -= 26

        liczba_do_dodania = chr(liczba_dodaj)
        new_napis += liczba_do_dodania
    return new_napis

def odszyfruj(napis: str, klucz: str):
    new_napis = ""
    dlugosc_klucza = klucz.__len__()
    for (idx, letter) in enumerate(napis):
        liczba_dodaj = ord(letter) - (ord(klucz[idx % dlugosc_klucza]) - ord('A') + 1)

        if liczba_dodaj < 65:
            liczba_dodaj += 26

        liczba_do_dodania = chr(liczba_dodaj)
        new_napis += liczba_do_dodania
    return new_napis

with open('tj.txt', 'r+') as fileSlowa:
    with open('klucze1.txt') as fileKlucze:
        with open('wynik4a.txt', 'w+') as fileOdpowiedz:
            slowa = fileSlowa.readlines()
            klucze = fileKlucze.readlines()

            for (idx,slowo) in enumerate(slowa):
                slowo = slowo[:-1]
                kluczNowy = klucze[idx][:-1]

                # print(slowo, kluczNowy)

                fileOdpowiedz.write(f"{szyfruj(slowo,kluczNowy)}\n")

with open('sz.txt', 'r+') as fileSlowa:
    with open('klucze2.txt') as fileKlucze:
        with open('wynik4b.txt', 'w+') as fileOdpowiedz:
            slowa = fileSlowa.readlines()
            klucze = fileKlucze.readlines()

            for (idx,slowo) in enumerate(slowa):
                slowo = slowo[:-1]
                kluczNowy = klucze[idx][:-1]

                # print(slowo, kluczNowy)

                fileOdpowiedz.write(f"{odszyfruj(slowo,kluczNowy)}\n")
