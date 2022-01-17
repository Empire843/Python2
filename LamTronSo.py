t = int(input())
while (t > 0):
    t -= 1
    n = input()
    if len(n) == 1:
        print(n)
    else:
        tmp = int(n[len(n) - 1])
        for i in range(len(n) - 1, -1, -1):
            if tmp >= 5:
                tmp = int(n[i]) + 1
            else:
                tmp = int(n[i])
        print(tmp * (10 ** (len(n) - 1)))
