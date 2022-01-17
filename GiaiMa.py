t = int(input())
while t > 0:
    t -= 1
    s = input()
    s1 = ""
    res = ""
    for i in s:
        if i >= 'A' and i <= 'Z':
            s1 = i;
        else:
            s1 = s1 * int(i)
            res = res + s1

    print(res)