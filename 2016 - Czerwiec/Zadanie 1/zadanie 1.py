def F(n):
    if n == 1 or n == 2:
        s = n
    else:
        s = n * F(n - 2)
    s = s * (n + 1)
    return s


def F2(n):
    print(f"F({n})")
    if n == 1 or n == 2:
        s = n
    else:
        s = n * F2(n - 2)
    s = s * (n + 1)
    return s


# for i in range(1, 7): # 1
#     print(i, F(i))
# F2(11) # 2
print(F(11)) # 3
