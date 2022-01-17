def SumOfNumber(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 10 == 0:
        return True
    else:
        return False


def solve(n):
    for i in range(1, len(n)):
        if abs(int(n[i]) - int(n[i - 1])) != 2:
            return "NO"
    if SumOfNumber(n) == True:
        return "YES"
    return "NO"


t = int(input())
while t > 0:
    t -= 1
    n = input()
    print(solve(n))
