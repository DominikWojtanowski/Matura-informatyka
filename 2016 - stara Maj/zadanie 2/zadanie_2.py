def adding(num: int) -> int:
    res = 0
    for i in range(num + 1):
        res += i
    return res

print()
print(adding(2))
print(adding(3))
print(adding(7))
print(adding(10))
print(adding(15))
print(adding(1000))