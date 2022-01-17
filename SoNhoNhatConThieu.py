n = int(input())
a = list(map(int,input().split()))
k = 0
for i in range(1, n+1):
    if a.count(i) == 0:
        print(i)
        k=1
        break
if k == 0:
    print(n+1)