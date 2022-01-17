while True:
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    else:
        if a[0] == a[1] == a[2] == a[3]:
            print(0)
        else:

            k = 0
            while True:
                k += 1
                tmp = a[0]
                for i in range(3):
                    a[i] = abs(a[i] - a[i + 1])
                a[3] = abs(a[3] - tmp)
                if a[0] == a[1] == a[2] == a[3]:
                    print(k)
                    break
