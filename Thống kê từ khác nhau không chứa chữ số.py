import re

n = int(input())
b = []
while n > 0:
    b.extend(re.findall(r'[a-zA-Z]+', input()))
    n -=1
c = []
dict = {}
for i in b:
    if i.lower() not in c:
        dict[i.lower()] = -1
        c.append(i.lower())
    else:
        temp = dict[i.lower()]
        dict[i.lower()] = temp - 1
sorted_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]))
for i in sorted_dict:
    print(i[0], abs(i[1]))
