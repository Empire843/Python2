def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)


x = input().split()
n = int(x[0])
k = int(x[1])
line = 0
for i in range(10 ** (k - 1), 10 ** k):
    if ucln(n,i) == 1:
        print(i,end = " ")
        line+=1
        if line == 10:
            print()
            line = 0
