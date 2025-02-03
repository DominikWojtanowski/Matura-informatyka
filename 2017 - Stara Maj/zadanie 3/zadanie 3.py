T = [0,6,2,-1,5,1,2]
s = 0
n = 3
i = 6

while i > n - 1:
    s = s + T[i]
    i = i - 1

print(s) # s = 7

# 2.
# P F F F

def otherToBase10(n, otherBase):
    res = 0
    for iter, i in enumerate(n[::-1]):
        liczba = ord(i) - ord('0')
        if liczba >= 10:
            res += (ord(i) - ord('A') + 10) * otherBase ** iter
        else:
            res += liczba * otherBase ** iter
    return res

# 3.3
print(150 < int('10011001',2))
print(150 < otherToBase10("1222",4))
print(150 < int('227',8))
print(150 < int('9B',16))

# 3.4
# PFPP

# 3.5
# FFPF

# 3.6
# FPFF