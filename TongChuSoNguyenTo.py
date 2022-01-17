import math


def isPrime(s):
    n = int(s)
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")