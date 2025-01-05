import math

with open('punkty.txt','r+') as file:
    COORDS = [line.replace('\n','').split(' ') for line in file.readlines()]
    ileNaBrzegu = 0
    ileW = 0
    r = 200
    a, b = 200, 200
    for idx, (x, y) in enumerate(COORDS, start=1):
        intX, intY = int(x), int(y)
        wynik = math.sqrt(math.pow(intX - a,2) + math.pow(intY - b, 2))
        if wynik == r:
            ileNaBrzegu += 1
            print(x, y)
        elif wynik < r and wynik >= 0:
            ileW += 1
        if idx == 100:
            print(ileW)
    print(ileNaBrzegu)
    print(ileW)

