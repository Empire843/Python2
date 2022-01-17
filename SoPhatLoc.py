t = int(input())
while t > 0:
    t -= 1
    n = input()
    if n[len(n) - 2] == '8' and n[len(n) - 1] == '6':
        print("YES")
    else:
        print("NO")
