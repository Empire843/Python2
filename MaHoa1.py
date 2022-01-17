t = int(input())
while t > 0:
    t -= 1
    s = input()
    count = 1
    res = ""
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            res = res + str(count) + s[i]
            count = 1
    res += str(count) + s[len(s) - 1]
    print(res)
