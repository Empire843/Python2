t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    tmp = k
    a = []
    f0 = 1
    f1 = 1
    a.append(f0)
    a.append(f1)
    while tmp > 0:
        tmp -= 1
        fn = f0 + f1
        f0 = f1
        f1 = fn
        a.append(fn)
    for i in range(n - 1, k):
        print(a[i], ' ', end="")
    print()
