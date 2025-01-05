poczatek = "Insert into panstwa(full_name, short_name) values"
with open("ps2txt","r") as f:
    lines = f.readlines()
    for line in lines:
        line = "'" + line[:-1] + "'"
        line = "".join(["','" if i == ";" else i for i in line])
        poczatek += f"({line}),";
poczatek = poczatek[:-1] + ";"
print(poczatek)
