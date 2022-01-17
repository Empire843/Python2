n = int(input())
for t in range(n):
    s = input()
    # Devide
    s1 = list(s[:len(s) // 2])
    s2 = list(s[len(s) // 2:])

    # Rotate
    sum1, sum2 = 0, 0
    for i in s1:
        sum1 += (ord(i) - 65)
    for i in s2:
        sum2 += (ord(i) - 65)
    for i in range(len(s1)):
        s1[i] = chr(65 + (sum1 + ord(s1[i]) - 65) % 26)
    for i in range(len(s2)):
        s2[i] = chr(65 + (sum2 + ord(s2[i]) - 65) % 26)

    # Merge
    for i in range(len(s1)):
        s1[i] = chr((ord(s1[i]) - 65 + ord(s2[i]) - 65) % 26 + 65)
    print("".join(s1))
