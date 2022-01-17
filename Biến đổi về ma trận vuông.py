n, m = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

if n > m:
    i = 0
    while n > m:
        del a[i]
        i+=1
        n-=1
if n < m:
    i = 1
    while n < m:
        for j in range(len(a)):
            del a[j][i]
        i+=1
        m-=1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end= " ")
    print()
# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9
# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7