def solve(n):
    sum = 0
    ans = 1
    k = 0
    for i in range(len(n)):
        if i != 0 and i % 2 != 0:
            sum += int(n[i])
        else:
            if n[i] != '0':
                k = 1
                ans *= int(n[i])
    if k == 0:
        ans = 0
    print(ans, sum)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)
