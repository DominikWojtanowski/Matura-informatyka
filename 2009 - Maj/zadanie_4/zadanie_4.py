import random
from typing import Tuple
def uklad1(x: float,y: float) -> Tuple[float,float]:
    return (0.76 * x - 0.4 * y, 0.4 * x + 0.76 * y)

def uklad2(x: float, y:float) -> Tuple[float,float]:
    return (-0.4 * x - 1, -0.4 * y + 0.1)

funTab = [uklad1,uklad2]

with open("zad4.txt", "w+") as file:
    x = 1
    y = 1


    file.write(f"{x} {y}\n")

    for i in range(5000):
        x, y = random.choice(funTab)(x,y)

        x_str = str(x)
        x_str = x_str.replace('.',',')

        y_str = str(y)
        y_str = y_str.replace('.', ',')

        file.write(f"{x_str} {y_str}\n")

with open('zad4.txt','r+') as file:
    x = 0
    y = 0
    min_x = 1000000
    max_x = -100000

    min_y = 1000000
    max_y = -10000000

    lines = file.readlines()

    lines = lines[100:]
    for line in lines:
        line = line[:-1]
        lineArr = line.split(" ")

        tmp_x = float(lineArr[0].replace(',','.'))
        tmp_y = float(lineArr[1].replace(',','.'))

        if tmp_x < min_x:
            min_x = tmp_x
        if tmp_x > max_x:
            max_x = tmp_x

        if tmp_y < min_y:
            min_y = tmp_y
        if tmp_y > max_y:
            max_y = tmp_y

        x += tmp_x
        y += tmp_y

    print(round(x / 4900,1))
    print(round(y / 4900,1))

    print(round(max_x,1), round(min_x,1))
    print(round(max_y,1), round(min_y,1))