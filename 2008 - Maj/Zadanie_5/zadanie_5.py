def checkIfPalindrom(w: str) -> bool:
    mid = w.__len__() // 2
    for i in range(mid):
        if w[i] != w[-1 - i]:
            return False
    return True

def createPassword(w: str) -> str:
    end = w.__len__() - 1

    isPalim = False
    while not isPalim and end >= 0:
        isPalim = checkIfPalindrom(w[:end + 1])
        end = end - 1

        if isPalim == True:
            end = end + 2

    other_str = w[end:]
    return other_str[::-1] + w

with open("slowa.txt", "r+") as file:
    with open("hasla_a.txt", "w+") as fileToWrite:
        max_password = ["", 0]
        min_password = ["", 20000000000000]

        lines = file.readlines()
        for line in lines:
            line = line[:-1]

            password = line[::-1]
            fileToWrite.write(f"{password}\n")

            if password.__len__() > max_password[1]:
                max_password[0] = password
                max_password[1] = password.__len__()
            if password.__len__() < min_password[1]:
                min_password[0] = password
                min_password[1] = password.__len__()

            with open("slowa_a.txt", "w+") as fileToWriteLengths:
                fileToWriteLengths.write(f"Najwiekszy lenght: {max_password[1]}, password: {max_password[0]}\n")
                fileToWriteLengths.write(f"Najmiejszy length: {min_password[1]}, password: {min_password[0]}")




with open("slowa.txt", "r+") as file:
    with open("hasla_b.txt", "w+") as fileToWrite:
        with open("slowa_b.txt", "w+") as fileToWriteLengths:
            fileToWriteLengths.write(f"1. \n")

            max_password2 = ["",0]
            min_password2 = ["",20000000000000]

            length_sum = 0

            lines = file.readlines()

            for line in lines:
                line = line[:-1]
                password = createPassword(line)

                if password.__len__() == 12:
                    fileToWriteLengths.write(f"{password}\n")

                length_sum += password.__len__()

                if password.__len__() > max_password2[1]:
                    max_password2[0] = password
                    max_password2[1] = password.__len__()
                if password.__len__() < min_password2[1]:
                    min_password2[0] = password
                    min_password2[1] = password.__len__()

                fileToWrite.write(f"{password}\n")

            fileToWriteLengths.write(f"2.\nNajwiekszy lenght: {max_password2[1]}, password: {max_password2[0]}\n")
            fileToWriteLengths.write(f"Najmiejszy length: {min_password2[1]}, password: {min_password2[0]}\n")

            fileToWriteLengths.write(f"3.\n{length_sum}\n")
