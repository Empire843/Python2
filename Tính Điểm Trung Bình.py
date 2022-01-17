n = int(input())
a = list(map(float, input().split()))
maxx = max(a)
minn = min(a)
i = 0
while i < len(a):
    if a[i] == maxx:
        del a[i]
    elif a[i] == minn:
        del a[i]
    else:
        i += 1
print(round(sum(a) / len(a), 2))

# print(a)
