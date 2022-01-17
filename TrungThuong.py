t = int(input())
while t > 0:
    t-=1
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort(reverse=False)
    Max = 0
    res = 0
    for i in range(0,n):
        if a.count(a[i]) > Max:
            Max = a.count(a[i])
            res = a[i]
    print(res)