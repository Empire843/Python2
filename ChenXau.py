s1 = input()
s2 = input()
p = int(input())
p -= 1
s3 = s1[0:p] + s2 + s1[p:len(s1)]
print(s3)
