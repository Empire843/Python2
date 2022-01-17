from builtins import input

t = int(input())
while t > 0:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=False)
    b.sort(reverse=False)
    k = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            print("NO")
            k += 1
            break
    if k == 0:
        print("YES")