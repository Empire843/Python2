t = int(input())
while t > 0:
    t-=1
    s = input()
    c = []
    num = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            num += int(s[i])
        else:
            c.append(s[i])
    c.sort(reverse=False)
    s1 = "".join(c)
    s1 += str(num)
    print(s1)