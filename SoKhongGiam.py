def solution(num):
    k = int(num[0])
    for i in num:
        if int(i) >= k:
            k = int(i)
        else:
            return 0
    return 1


t = int(input())
while t > 0:
    num = input()
    t -= 1
    if solution(num) == 1:
        print("YES\n")
    else:
        print("NO\n")
