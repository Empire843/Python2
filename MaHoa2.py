p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
k = 1
while True:
    x = input().split()
    k = int(x[0])
    if k == 0:
        break
    s = x[1]
    res = ""
    for i in s:
        if i != '.' and i != '_':
            res = p[((ord(str(i)) - 65) + k) % 28] + res
        if i == '_':
            res = p[(26 + k) % 28] + res
        if i == '.':
            res = p[(27 + k) % 28] + res
    print(res)
# ord("A") chuyển sang asscii
