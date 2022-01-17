n = int(input())
a = []
while len(a) < n:
    tmp = list(map(int, input().split()))
    a +=tmp
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
b.sort(reverse=False)
c.sort(reverse=True)
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(b.pop(0),end = " ")
    else:
        print(c.pop(0), end = " ")