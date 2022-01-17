def solve(n):
    tmp = n[0]
    if len(n) % 2 == 0:
        return "NO"
    if int(n[0]) == int(n[1]):
        print(2)
        return "NO"
    for i in range(len(n)):
        if i % 2 == 0 or i == 0:
            if n[i] != tmp:
                print(3)
                return "NO"
    return "YES"

t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))