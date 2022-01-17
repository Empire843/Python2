t = int(input())
while t > 0:
    t -= 1
    n = input()
    k = 0
    for i in n:
        if int(i) != 4 and int(i) != 7:
            print("NO")
            k += 1
            break
    if k == 0:
        print("YES")
