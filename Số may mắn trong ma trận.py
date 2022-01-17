

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

maxNumber = -1
minNumber = 999999
for i in range(n):
    # print(max(a[i]), min(a[i]))
    if max(a[i]) > maxNumber:
        maxNumber = max(a[i])
    if min(a[i]) < minNumber:
        minNumber = min(a[i])

res = maxNumber - minNumber
k = 0
for i in range(n):
    if res not in a[i]:
        continue
    else:
        k = 1
        break
if k == 0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j] == res:
                print(f"Vi tri [{i}][{j}]")

