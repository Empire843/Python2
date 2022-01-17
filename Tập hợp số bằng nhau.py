n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1, b1 = [], []
for i in a:
    if i not in a1:
        a1.append(i)
for i in b:
    if i not in b1:
        b1.append(i)
a1.sort(reverse=False)
b1.sort(reverse=False)
if a1 == b1:
    print("YES")
else:
    print("NO")