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
while t > 0:
    t -= 1
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    c = str(uscln(a, b))
    sum = 0
    for i in c:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
