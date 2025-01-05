def sklej(n: int):
    if n == 1:
        return 0
    elif n % 2 == 0:
        # print(f"sklej({n}): {n - 1 + 2 * sklej(n//2)}")
        return n - 1 + 2 * sklej(n//2)
    elif n % 2 == 1:
        # print(f"sklej({n}): {n - 1 + sklej((n - 1) // 2) + sklej((n + 1) // 2)}")
        return n - 1 + sklej((n - 1) // 2) + sklej((n + 1) // 2)



i = 10

s = [0] * (i + 1)
s[0] = 0
s[1] = 0
s[2] = 1

for i in range(1, i + 1):
    if i % 2 == 0:
        s[i] = i - 1 + 2 * s[i//2]
    else:
        s[i] = i - 1 + s[(i - 1) // 2] + s[(i + 1) // 2]

print(s)


