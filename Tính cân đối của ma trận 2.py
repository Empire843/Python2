def inputArray(n):
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    return a


n = int(input())
a = inputArray(n)
k = int(input())
sumTop = 0
sumBottom = 0

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            sumTop += a[i][j]
        elif j > n - i - 1:
            sumBottom += a[i][j]
if abs(sumTop - sumBottom) <= k:
    print("YES")
    print(abs(sumTop - sumBottom))
else:
    print("NO")
    print(abs(sumTop - sumBottom))
