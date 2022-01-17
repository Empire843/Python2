n = int(input())
a = []
for t in range(n):
    s = input()
    num = ""
    for i in range(len(s)):
        if s[i].isnumeric():
            num += s[i]
        else:
            if num != "":
                a.append(int(num))
            num = ""
    if num != "":
        a.append(int(num))
a.sort(reverse=False)
for i in a:
    print(i)
# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa