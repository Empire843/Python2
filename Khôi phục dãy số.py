n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res = []
if (n == 2):
    print(1, 1)
else:
    x0, x1, x2 = 0, 0, 0
    x0 = a[0][1] -  ((a[0][1] - a[0][2] + a[1][2]) // 2)
    res.append(x0)

    for i in range(1, n):
        x = a[0][i] - res[0]
        res.append(x)
    for i in res:
        print(i, end=" ")

"""
4
0 4 2 5
4 0 3 4
2 3 0 9
5 4 9 0

2 2 1 8
"""
