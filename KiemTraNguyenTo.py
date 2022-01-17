import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


x = input().split()
n = int(x[0])
m = int(x[1])
matrix = []
row = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(m):
        if isPrime(matrix[i][j]) == True:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
for i in range(n):
    for j in matrix[i]:
        print(j, " ", end="")
    print()
