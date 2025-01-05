def algo(arr: list):
    i = 0
    wynik = 0
    for num in arr:
        x = num
        wynik = (i * wynik + x)/(i + 1)
        i += 1
    return wynik

print(algo([2,2,5,7]))


print(bin(ord('3')))
print(bin(ord('4')))
print(bin(ord('f')))

# print(bin(192))

# print(1024 * 768 * 8 / 8)