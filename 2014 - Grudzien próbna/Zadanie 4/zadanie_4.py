import math
from decimal import Decimal, getcontext

def x(r: float, t: Decimal, T: float) -> float:
    return r * math.sin((2 * math.pi * float(t)) / T)

def y(r: float, t: Decimal, T: float) -> float:
    return r * math.cos((2 * math.pi * float(t)) / T)


getcontext().prec = 3

r = 5
T = 12.5
krok:Decimal = Decimal(0.05)

t_pocz:Decimal = Decimal(3)
t:Decimal = t_pocz

xVar = 0
yVar = 0

while xVar >= yVar:
    xVar = x(r,t,T)
    yVar = y(r,t,T)

    if yVar <= xVar:
        t += krok
print(xVar,yVar,t)
print(x(r,Decimal(7.85), T))
print(y(r,Decimal(7.85),T))
