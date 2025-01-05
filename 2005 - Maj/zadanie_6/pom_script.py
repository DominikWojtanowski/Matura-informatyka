# city_id = "1,"
city_id=""

with open("pom_data","r") as f:
    lines = f.readlines()
    with open("new_data", "w") as nf:
        for idx,line in enumerate(lines, start=1):
            line = line[:-1]
            new_line = city_id + "".join(["," if i == " " else "." if i == "," else i for i in line])
            new_line = new_line
            nf.write(f"({new_line}),")