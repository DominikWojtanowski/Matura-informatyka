from math import *

def logarytm_zadanie(x: int):
    res = 0
    for i in range(x):
        res += (1/(2 * (i + 1) + 1)) * (1/(9 ** (i+1)))
    res += 1
    res *= (2/3)

    return  res
for i in range(4):
    print(f"{i}: {logarytm_zadanie(i)}")

def logarytm_zadanie(x: float) -> float:
    """i don't fucking unterstand it????"""
    isEnd = False
    l_n_min_1 = 2/3
    l = 0
    i = 0
    while not isEnd:
        i += 1
        l = l_n_min_1 + (2/3) * ((1/(2 * (i) + 1)) * (1/9**(i)))

        print(f"l_curr: {l}\n l_n-1: {l_n_min_1}")

        if abs(l - l_n_min_1) < x:
            print(abs(l - l_n_min_1))
            isEnd = True

        l_n_min_1 = l

    return l

print(logarytm_zadanie(0.000001))



