import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n, m = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
maxPrime = -1
for i in range(n):
    if max(a[i]) > maxPrime and isPrime(max(a[i])):
        maxPrime = max(a[i])
if maxPrime == -1:
    print("NOT FOUND")
else:
    print(maxPrime)
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")