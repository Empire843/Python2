import math


def isPrime(x):
    n = int(x)
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    sizeN = len(n) - 1
    s = ""
    s = s + n[sizeN - 3] + n[sizeN - 2] + n[sizeN - 1] + n[sizeN];
    if isPrime(s):
        return "YES"
    else:
        return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
