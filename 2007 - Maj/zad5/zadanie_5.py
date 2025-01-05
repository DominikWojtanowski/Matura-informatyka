def num_to_binary(n: int) -> str:
    if n == 0:
        return '0'

    binary_digits = []
    while n != 0:
        binary_digits.append(str(n % 2))
        n //= 2

    return "".join(binary_digits[::-1])

def checkIfPrime(n: int) -> bool:
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False

        i += 6

    return True

def sumNumSysTen(n: int) -> int:
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


def sumBinaryNumbers(n: str) -> int:
    sum = 0
    for i in n[::-1]:
        sum += ord(i) - ord('0')
    return sum

def checkIfSuperBPrime(n: int) -> bool:
    if not checkIfPrime(n):
        return False
    if not checkIfPrime(sumNumSysTen(n)):
        return False
    if not checkIfPrime(sumBinaryNumbers(num_to_binary(n))):
        return False
    return True



with open("1.txt","w+") as file:
    sum = 0
    for i in range(2,1001):
        if checkIfSuperBPrime(i):
            file.write(f"{i}\n")
            sum += 1
    print(sum)

with open("2.txt","w+") as file:
    sum = 0
    for i in range(100,10001):
        if checkIfSuperBPrime(i):
            file.write(f"{i}\n")
            sum += 1
    print(sum)
    print(checkIfPrime(sum))

with open("3.txt","w+") as file:
    sum = 0
    for i in range(1000,100001):
        if checkIfSuperBPrime(i):
            file.write(f"{i}\n")
            sum += 1
    print(sum)



