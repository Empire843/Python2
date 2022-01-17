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
    count = 0
    for i in range(len(n)):
        if isPrime(int(n[i])):
            count += 1
    if isPrime(len(n)) and count > (len(n) / 2):
        return "YES"
    return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
