t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    a.sort(reverse=False)
    for i in range(n):
        if a[i] not in dict:
            dict[a[i]] = 1
        else:
            tmp = dict[a[i]]
            dict[a[i]] = tmp + 1
    # print(dict, sep="\n")
    for i in dict:
        if dict[i] % 2 != 0:
            print(i)
            break
    # print(dict)
