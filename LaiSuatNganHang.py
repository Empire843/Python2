t = int(input())
while t > 0:
    t -= 1
    a = list(map(float, input().split()))
    n = a[0]
    x = a[1]
    m = a[2]
    i = 0
    while n < m:
        i += 1
        n = n + n * (x / 100)
        # print(n)
    print(i)
