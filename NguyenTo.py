import math


def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);


def isPrime(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 0
    return 1


t = int(input())
while (t > 0):
    t -= 1
    k = 0
    n = int(input())
    for i in range(1, n):
        if uscln(i, n) == 1:
            k += 1
    if isPrime(k) == 1:
        print("YES")
    else:
        print("NO")
