n = int(input())
a = [];
x = 0
while x < n:
    x+=1
    tmp = list(map(int,input().split()))
    a.append(tmp)
k = int(input())
sumTop = 0
sumBottom = 0
for i in range(n):
    for j in range(n):
        if j > i:
            sumTop+=a[i][j]
        elif j < i:
            sumBottom+=a[i][j]
if abs(sumTop - sumBottom) > k:
    print("NO",abs(sumTop - sumBottom),sep = "\n")
else:
    print("YES", abs(sumTop - sumBottom),sep = "\n")
# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5