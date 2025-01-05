city_id = 2

with open("new_data", "w") as fx:
    pass

with open("data.txt", "r+") as f:
    with open("new_data", "a+") as f2:
        for (i,line) in enumerate(f.readlines(), start=1):

            idx = line.find(" ")
            line = str(i) + "," + line[:idx] + " " + str(city_id) + line[idx:]
            line = "".join(["," if i == " " else i for i in line])
            f2.write(line)