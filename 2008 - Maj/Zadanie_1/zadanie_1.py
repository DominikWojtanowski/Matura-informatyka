def alghorithm(a: int, n: int) -> int:
    if n == 1:
        return a
    else:
        a_przez_2 = alghorithm(a, n//2)

        return a_przez_2 * a_przez_2


# values = [2,4,8,6]
# k = 0
#
# for k in range(0, 16):
#     a_k = 1 if k == 0 else values[(k - 1) % 4]
#     print(f"{a_k}",end=", ")

print(alghorithm(2,16))
