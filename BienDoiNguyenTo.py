import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
prime = [2]
b = []
for i in a:
    if isPrime(i) == False:
        b.append(i)
b.sort()
for i in range(3, 10001):
    if isPrime(i):
        prime.append(i)

pos = 0
res = 0
ans = 0
for i in range(len(b)):
    for j in range(pos, len(prime)):
        if prime[j] < b[i] and b[i] < prime[j + 1]:
            # print(prime[j], b[i], prime[j + 1])
            pos = j
            ans = min(abs(prime[j] - b[i]), abs(prime[j + 1] - b[i]))
            res = max(ans,res)
print(res)
