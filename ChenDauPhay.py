s = input()
k = 0
res = ""
for i in range(len(s) - 1, 0, -1):
    k+=1
    res = s[i] + res
    if k == 3:
        res = ',' + res
        k = 0
res = s[0] + res
print(res)