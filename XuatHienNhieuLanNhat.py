def solve(a, n):
    dict = {}
    for i in a:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    maxx = -999999999999999999999999999
    pos = -1
    for key, value in dict.items():
        if value > maxx:
            maxx = value
            pos = key
    if maxx <= (len(a) // 2):
        return "NO"
    else:
        return str(pos)

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a, n))
