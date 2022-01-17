import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    for i in range(len(n)):
        if i == 0 or i % 2 == 0:
            if int(n[i]) % 2 != 0:
                return "NO"
        elif i == 1 or i % 2 != 0:
            if int(n[i]) % 2 == 0:
                return "NO"
    sum = 0
    for i in n:
        sum += int(i)
    if isPrime(sum) == False:
        return "NO"
    return "YES"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
