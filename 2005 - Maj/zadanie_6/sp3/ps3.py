zawodnik_punkt = []

with open("ps3.txt", "r" ) as f:
    lines = f.readlines()
    with open("ps3pom.txt", "w") as nf:
        for line in lines:
            line = "".join(["." if i == "," else i for i in line])
            line = line[:-1]
            nf.write(f"{line}\n")

with open("ps3pom.txt", "r" ) as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        print(line)
        line_tab = line.split(" ")
        print(line_tab)
        print(int(line_tab[0]))
        # line_tab = line.split(" ")
        # print(line[2],line[-1])
        # zawodnik_punkt.append([line[0], float(line[2]) + float(line[-1])])
print(zawodnik_punkt)


