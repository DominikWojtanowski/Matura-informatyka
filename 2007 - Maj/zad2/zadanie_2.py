xy = list(map(int, input("podaj wartosci po przecinku:\n").split(" ")))

rozmiar_planszy = int(input("Podaj rozmiar planszy:\n"))

x = rozmiar_planszy - 1
y = rozmiar_planszy - 1

skos_lewo_gora = min(xy[0]-1, rozmiar_planszy - xy[1])
skos_lewo_dol = min(rozmiar_planszy - xy[0], xy[1] - 1)

skos_prawo_gora = min(rozmiar_planszy - xy[1], rozmiar_planszy - xy[0])
skos_prawo_dol = min(xy[1] - 1, xy[0] - 1)

print(x + y + skos_lewo_gora + skos_lewo_dol + skos_prawo_gora + skos_prawo_dol)


