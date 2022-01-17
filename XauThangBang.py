t = int(input())
while t > 0:
    t -= 1
    s = input()
    s1 = s[::-1]
    k = 0
    # print(s)
    # print(s1)
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s1[i]) - ord(s1[i - 1])):
            # print(s[i] + ' ' + s[i - 1] + ' ' + s1[i] + ' ' + s1[i - 1])
            # print(ord(s[i]), ' ', ord(s[i - 1]), ' ', ord(s1[i]), ' ', ord(s1[i - 1]))
            print("NO")
            k += 1
            break
    if k == 0:
        print("YES")
# s = 'a'
# k = ord(s)
# print(k)
