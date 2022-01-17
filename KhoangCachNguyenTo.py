import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


k = input().split()
n = int(k[0])
x = int(k[1])
a = []
p = n
i = 2
while True:
    if isPrime(i):
        p -= 1
        a.append(i)
    if p == 0:
        break
    i += 1
i = 0
print(x, ' ', end="")
while n > 0:
    n -= 1
    print(x + a[i], ' ', end="")
    x = x + a[i]
    i += 1
