import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if isPrime(a[i]) == True:
        # if a[i] not in b:
            b.append(a[i])
    else:
        continue
b.sort(reverse=False)
for i in range(n):
    if isPrime(a[i]) == True:
        a[i] = b.pop(0)
for i in a:
    print(i,end = " ")
