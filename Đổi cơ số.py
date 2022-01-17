t = int(input())
char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
while t > 0:
    t -= 1
    n, b = list(map(int, input().split()))
    a = []
    while n > 0:
        a.append(n % b)
        n//=b
    # print(a)
    for i in range(len(a)):
        if a[i] >= 10:
            a[i] = char[a[i] - 10]
    for i in range(len(a) - 1,-1,-1):
        print(a[i],end = "")
    print()
