import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
Sum_b = sum(b)
Sum_sub = 0
k = 0
for i in range(len(b)):
    Sum_sub += b[i];
    if isPrime(Sum_sub) and isPrime(Sum_b - Sum_sub):
        print(i)
        k =1
        break
if k == 0:
    print("NOT FOUND")