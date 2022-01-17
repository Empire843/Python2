import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


n = int(input())
a = list(map(int, input().split()))
# for i in a:
#     if isPrime(i) == False:
#         print(i)
#         a.remove(i)
# print(a)
for i in range(n):
    if isPrime(a[i]) == False:
        continue
    k = a.count(a[i])
    x = a[i]
    a[i] = 0
    for j in range(i+1,n):
        if x == a[j]:
            a[j] = 0
    print(x, ' ', k)
print()

