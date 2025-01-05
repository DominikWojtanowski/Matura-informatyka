ilosc_dni_pozytywnych = 0
poprawiony_wynik = 0

# a
tmp_ilosc = 0
iloscDniPozytywnychWiekszychNiz3 = 0

# b
min = 10000000000000000000000000
max = 0

# c
maksymalnyCiagDni = 0
roznicaDlaMaksCiagu = 0

obecnyCiagDni = 0
poczatkowySkok = 0
koncowySkok = 0

pozytywnyCiagDni = 0
poczatkowySkokZad1 = 0
koncowySkokZad1 = 0

line_arr = []

with open('dziennik.txt','r+') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]

        intLine = int(line)
        line_arr.append(intLine)

        if intLine > max:
            max = intLine
        if intLine < min:
            min = intLine

    for i in range(line_arr.__len__()-1):
        if line_arr[i] < line_arr[i + 1]:
            if pozytywnyCiagDni == 0:
                poczatkowySkokZad1 = line_arr[i]
            pozytywnyCiagDni += 1
        else:
            pozytywnyCiagDni += 1
            if pozytywnyCiagDni > 3:
                koncowySkokZad1 = line_arr[1]
                if koncowySkokZad1 - poczatkowySkokZad1 > 0:
                    iloscDniPozytywnychWiekszychNiz3 += 1
                    print(poczatkowySkokZad1, koncowySkokZad1)

            koncowySkokZad1 = 0
            poczatkowySkokZad1 = 0
            pozytywnyCiagDni = 0


    for i in range(line_arr.__len__()-1):
        if line_arr[i] < line_arr[i + 1]:
            if obecnyCiagDni == 0:
                poczatkowySkok = line_arr[i]
                obecnyCiagDni += 1
            else:
                obecnyCiagDni += 1
        else:
            obecnyCiagDni += 1
            if obecnyCiagDni > maksymalnyCiagDni:
                koncowySkok = line_arr[i]
                maksymalnyCiagDni = obecnyCiagDni
                roznicaDlaMaksCiagu = koncowySkok - poczatkowySkok

            obecnyCiagDni = 0
            poczatkowySkok = 0
            koncowySkok = 0

    print(iloscDniPozytywnychWiekszychNiz3)
    print(max,min)
    print(maksymalnyCiagDni, roznicaDlaMaksCiagu)