def condition(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int,input().split()))
    b = {}
    for i in a:
        x = i
        b[i] = condition(i)
    sort_b = sorted(b.items(),key = lambda x:(x[1],x[0]))
    for i in sort_b:
        print(i[0],end = " ")
    print()
