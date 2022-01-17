n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
dict = {}
for i in range(n):
    if a[i] not in dict:
        dict[a[i]] = -1
    else:
        tmp = dict[a[i]]
        dict[a[i]] = tmp - 1
sorted_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]), reverse=False)
Max = max(sorted_dict, key=lambda x: abs(x[1]))
k = 0
for i in sorted_dict:
    if abs(i[1]) == abs(Max[1]):
        continue
    else:
        k = 1
        print(i[0])
        break
if k == 0:
    print("NONE")
