def thuanNghich(n):
    if(len(n) <=1):
        return "NO"
    if n == n[::-1]:
        return "YES"
    else:
        return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    print(thuanNghich(str(sum)))
