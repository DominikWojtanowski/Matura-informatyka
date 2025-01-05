import math

with open('punkty.txt','r+') as file:
    COORDS = [line.replace('\n','').split(' ') for line in file.readlines()]
    bledyBezwzgledne = [0]
    COORDS = COORDS[:1700]
    ileWOkregu = 0
    ileWKwadracie = 0
    poleKwadratu = 400 * 400
    pi = 0
    r = 200
    a, b = 200, 200
    for idx, (x, y) in enumerate(COORDS, start=1):
        intX, intY = int(x), int(y)
        wynik = math.sqrt(math.pow(intX - a,2) + math.pow(intY - b, 2))
        if wynik <= r and wynik >= 0:
            ileWOkregu += 1
        ileWKwadracie += 1

        pi = (ileWOkregu * poleKwadratu) / (ileWKwadracie * (r ** 2))
        bledyBezwzgledne.append(abs(math.pi - pi))
        print(str(round(abs(math.pi - pi),4)).replace('.',','))
    print()
    # print(bledyBezwzgledne)
    # print(round(bledyBezwzgledne[1000],4))
    # print(round(bledyBezwzgledne[1700],4))
