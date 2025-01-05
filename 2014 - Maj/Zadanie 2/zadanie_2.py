def sign(liczba: float) -> float:
    return 1 if liczba >= 0 else 0

def f(x: float) -> float:
    return x ** 3 - x - 2

def binaryRangeSearch(a: int, b: int) -> int:
    x0 = False
    i = 1
    while not x0:

        x = (a + b) / 2

        fx = f(x)
        if fx != 0:
            fa = f(a)
            fb = f(b)

            i+=1

            print(f"{i}, a: {a}, b: {b}, fa: {fa}, fb: {fb}, x: {x}, fx:{fx}")
            if b - a < 0.1:
                print(i)
                break

            if sign(fa) == sign(fx):
                a = x
            elif sign(fb) == sign(fx):
                b = x


        else:
            return x

def binaryRangeSearchWithD(a: float, b: float, d:float):
    x0 = False

    while not x0:
        if d > (b - a):
            break

        x = (a + b) / 2

        fx = f(x)
        if fx != 0:
            fa = f(a)
            fb = f(b)

            if sign(fa) == sign(fx):
                a = x
            elif sign(fb) == sign(fx):
                b = x

            if fa * fb > 0:
                break
        else:
            return x




print(binaryRangeSearch(1,2))
print()





