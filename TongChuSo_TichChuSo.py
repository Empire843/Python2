def solve(n):
    sum = 0
    ans = 1
    k = 0
    for i in range(len(n)):
        if i == 0 or i % 2 == 0:
            sum += int(n[i])
        else:
            if n[i] != '0':
                k = 1
                ans *= int(n[i])
    if k == 0:
        ans = 0
    print(sum, ans)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)
