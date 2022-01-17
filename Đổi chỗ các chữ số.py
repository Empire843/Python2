def solution(s1):
    s = list(s1)
    i = len(s) - 2
    while i >= 0 and s[i] <= s[i + 1]:
        i = i - 1
    if (i >= 0):
        max = i + 1
        for j in range(i + 1, len(s)):
            if s[j] < s[i] and s[j] > s[max]:
                max = j
        s[max], s[i] = s[i], s[max]
        if s[0] == '0':
            return -1
        else:
            return "".join(s)
    return -1


t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(solution(s))
