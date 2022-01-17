n = int(input())
a = []
while n > 0:
    n-=1
    s = input().split()
    for i in s:
        a.append(i)
dict = {}
for i in a:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1
dict_sorted = sorted(dict.items(),key = lambda x: (x[1],x[0]))
maxs = 0
maxs1 = 0
for i in dict_sorted:
    if i[1] > maxs:
        maxs1 = maxs
        maxs = i[1]
for k,v in dict.items():
    if v == maxs1:
        print(k,end =" ")
print()