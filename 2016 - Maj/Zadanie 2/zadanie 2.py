from typing import List
def fun(A: List[int]): # Better to do this in exam paper, this takes too much time
    klucz = A[1]
    w = 1
    for k in range(2,len(A)):
        if A[k] < klucz:
            tmp = A[k]
            A[k] = A[w]
            A[w] = tmp
            w += 1
    print(w)
    print(A[1])
    print(A[2])
    print(A[3])
    print(A)

A = [0,10,20,30,40,50,60,70,80,90,100,9,19,29,39,49,59,69,79,89,99,8,18,28,38,48,58,68,78,88,98,7,17,27,37,47,57,67,77,87,97,6,16,26,36,46,56,66,76,86,96,5,15,25,35,45,55,65,75,85,95,4,14,24,34,44,54,64,74,84,94,3,13,23,33,43,53,63,73,83,93,2,12,22,32,42,52,62,72,82,92,1,11,21,31,41,51,61,71,81,91]
fun(A)