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
    s1 ,s2= "",""
    s1 = s1 + n[sizeN - 2] + n[sizeN - 1] + n[sizeN];
    s2 = s2 + n[0] + n[1] + n[2]
    if isPrime(s1) and isPrime(s2):
        return "YES"
    else:
        return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
