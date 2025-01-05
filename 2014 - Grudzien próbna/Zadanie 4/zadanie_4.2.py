import math

def x(r: float, t: float, T: float) -> float:
    return r * math.sin((2 * math.pi * t) / T)

def y(r: float, t: float, T: float) -> float:
    return r * math.cos((2 * math.pi * t) / T)

def r(v: float, t: float) -> float:
    return v * float(t)

T = 10
v = 1

t_end = 10




t: float = 0
t_step: float = 0.5

xyArr = []
while t <= t_end:
    xVar = x(r(v,t), t, T)
    yVar = y(r(v,t), t, T)
    # print(str(xVar).replace('.',','), str(yVar).replace('.',','))


    xyArr.append([xVar,yVar])

    t += t_step

d = 0

for i in range(xyArr.__len__() - 1):
    print(xyArr[i])
    d += math.sqrt(math.pow(xyArr[i+1][0] - xyArr[i][0],2) + math.pow(xyArr[i+1][1] - xyArr[i][1], 2))

print(d)