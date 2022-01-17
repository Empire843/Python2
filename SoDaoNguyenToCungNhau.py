def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)


def solve(n):
    s = n[::-1]
    if ucln(int(s), int(n)) == 1:
        return "YES"
    return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solve(s))
