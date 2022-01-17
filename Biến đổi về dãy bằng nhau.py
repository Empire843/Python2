n = int(input())
a = list(map(int, input().split()))

sum = 0
res = 99999999999999999999999999999
pos = 0
for i in range(len(a)):
    sum = 0
    for j in range(len(a)):
        sum += abs(a[i]-a[j])
    if res > sum:
        res = sum
        pos = a[i]
print(res,pos)