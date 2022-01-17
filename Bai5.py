n = int(input())
dict1 = {}
while n > 0:
    n-=1
    s = input().split()
    for i in s:
        if i not in dict1.keys():
            dict1[i] = -1
        else:
            dict1[i] -= 1
lens = 0
for i in dict1.values():
    lens+=i
dict = {}
dict_sorted = sorted(dict1.items(),key = lambda x: (x[1],x[0]))
for i in dict_sorted:
    print(i[0],"%.2f"%(i[1]/lens))
