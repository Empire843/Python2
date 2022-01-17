s = input()
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
for i in dict:
    print(i,dict[i], end="\n")
