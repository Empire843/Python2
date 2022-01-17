s = input()
k = int(input())
lens = len(s)
if lens % 2 != 0:
    lens -= 1
dict = {}
for i in range(1, lens, +2):
    tmp = s[i - 1] + s[i]
    # print(tmp)
    if tmp not in dict:
        dict[tmp] = 1
    else:
        dict[tmp] += 1
p = 0
sort_dict = sorted(dict.items(),key=lambda x:(x[0],x[1]))
for i in sort_dict:
    if i[1] >= k:
        p = 1
        print(i[0],i[1], end="\n")
if p == 0:
    print("NOT FOUND")