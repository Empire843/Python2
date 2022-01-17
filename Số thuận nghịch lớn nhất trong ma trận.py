def TN(n):
    s = str(n)
    if s == s[::-1] and len(s) > 1:
        return True
    return False


n, m = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
maxTN = -1
for i in range(n):
    for j in range(len(a[i])):
        if TN(a[i][j]) == True and a[i][j] > maxTN:
            # print(maxTN)
            maxTN = a[i][j]
if maxTN == -1:
    print("NOT FOUND")
else:
    print(maxTN)
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j] == maxTN:
                print(f"Vi tri [{i}][{j}]")
