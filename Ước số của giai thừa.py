t = int(input())
while t > 0:
    t -= 1
    n, p = list(map(int, input().split()))
    count = 0
    for i in range(1, n + 1):
        if i % p == 0 and i >= p:
            tmp = i
            while tmp % p == 0:
                count = count + 1
                tmp //= p
    print(count)
