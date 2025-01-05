import math

iloscTrawy = 10000

iloscZgromadzonejTrawyWDniachRound = [0] * 214
iloscZgromadzonejTrawyWDniach = [0] * 214
iloscZmniejszenia = [0] * 214

iloscSamochodow = 30
pojemnoscSamochodow = 15

iloscZdobytejTrawy = (600 - (iloscSamochodow * 15))

iloscZgromadzonejTrawyWDniachRound[1] = 10000 + iloscZdobytejTrawy
iloscZgromadzonejTrawyWDniach[1] = 10000 + iloscZdobytejTrawy
iloscZmniejszenia[0] = 0
iloscZmniejszenia[1] = 0

warunek = False
dzien = 0

Zero12kwietnia = False

for i in range(2,214):
    iloscZgromadzonejTrawyWDniachRound[i] = math.floor(iloscZgromadzonejTrawyWDniachRound[i - 1] * 0.97) + iloscZdobytejTrawy
    iloscZgromadzonejTrawyWDniach[i] = iloscZgromadzonejTrawyWDniach[i - 1] * 0.97 + iloscZdobytejTrawy

    iloscZmniejszenia[i] = math.floor(iloscZgromadzonejTrawyWDniach[i - 1] - iloscZgromadzonejTrawyWDniach[i]) + iloscZdobytejTrawy

    if iloscZgromadzonejTrawyWDniachRound[i] == iloscZgromadzonejTrawyWDniachRound[i - 1] and not warunek:
        dzien = i - 1
        warunek = True

print(dzien)
print(iloscZmniejszenia[10])

while not Zero12kwietnia:
    iloscSamochodow += 1
    pojemnoscSamochodow = 15

    iloscZdobytejTrawy = (600 - (iloscSamochodow * 15))

    iloscZgromadzonejTrawyWDniachRound[1] = (10000 + iloscZdobytejTrawy) - math.floor((10000 + iloscZdobytejTrawy) * 0.03)

    for i in range(2, 13):
        iloscZgromadzonejTrawyWDniachRound[i] = (iloscZgromadzonejTrawyWDniachRound[i-1] + iloscZdobytejTrawy) - math.floor((iloscZgromadzonejTrawyWDniachRound[i-1] + iloscZdobytejTrawy) * 0.03)

    iloscZgromadzonejTrawyWDniachRound[12] = iloscZgromadzonejTrawyWDniachRound[11]
    if iloscZgromadzonejTrawyWDniachRound[12] - (iloscSamochodow * 15)<= 0:
        Zero12kwietnia = True
        print(iloscSamochodow)

# To jest raczej lepszy algorytm do tego
startowaIloscTrawy = [10000,7000,4000]
endDay = 101

endAmount = []
iloscZdobytejTrawy = 150


for startAmount in startowaIloscTrawy:
    iloscZgromadzonejTrawyWDniachRound[1] = (startAmount + iloscZdobytejTrawy) - math.floor((startAmount + iloscZdobytejTrawy) * 0.03)

    for i in range(2, 101):
        iloscZgromadzonejTrawyWDniachRound[i] = (iloscZgromadzonejTrawyWDniachRound[i - 1] + iloscZdobytejTrawy) - math.floor((iloscZgromadzonejTrawyWDniachRound[i - 1] + iloscZdobytejTrawy) * 0.03)
    iloscZgromadzonejTrawyWDniachRound[101] = iloscZgromadzonejTrawyWDniachRound[100]
    print(iloscZgromadzonejTrawyWDniachRound[101])





