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
    for i in range(len(n)):
        if (((isPrime(i) == True) and (isPrime(n[i]) == False)) or ((isPrime(i) == False) and (isPrime(n[i]) == True))):
            return "NO"
    return "YES"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
