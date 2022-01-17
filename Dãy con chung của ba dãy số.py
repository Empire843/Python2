t = int(input())
while t > 0:
    t -= 1
    x = input().split()
    n, m, p = int(x[0]), int(x[1]), int(x[2])
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    tmp = []
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b) and k < len(c):
        if (a[i] == b[j] and b[j] == c[k]):
            tmp.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    if not tmp:
        print("NO")
    else:
        for i in tmp:
            print(i, end=" ")
        print()
