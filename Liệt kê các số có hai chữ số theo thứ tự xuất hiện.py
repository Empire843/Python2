s = input()
lens = len(s)
if lens % 2 != 0:
    lens -= 1
b = []
for i in range(1, lens, +2):
    tmp = s[i - 1] + s[i]
    # print(tmp)
    if tmp not in b:
        b.append(tmp)
for i in b:
    print(i, end=" ")
