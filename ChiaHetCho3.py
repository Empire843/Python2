def Mod3(s):
    sum = 0
    for i in s:
        sum+=int(i)
    if sum % 3 == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(Mod3(s))