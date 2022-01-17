x = input().split()
a = int(x[0])
k = int(x[1])
n = int(x[2])
sum = a//k+1
p = 0
while sum:
    if k * sum <= n:
        print(k * sum - a, end=" ")
        p = 1
        sum+=1
    else:
        break
if p == 0:
    print("-1",end = " ");
print()
