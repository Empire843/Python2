s = input()
tmp = ""
k = 0
for i in range(len(s) - 1,-1,-1):
    if s[i] == '6':
        tmp = ""
        continue
    elif s[i] == '8':
        tmp = s[i] + tmp
        if len(tmp) >= 3:
            print("NO")
            k = 1
            break
    else:
        print("NO")
        k = 1
        break
if k == 0:
    print("YES")
