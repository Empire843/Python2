def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)


x = input().split()
L = int(x[0])
R = int(x[1])
for i in range(L, R - 1):
    for j in range(i + 1, R):
        for k in range(j + 1, R + 1):
            if ucln(i, j) == 1 and ucln(j, k) == 1 and ucln(i, k) == 1:
                print(i, j, k)
