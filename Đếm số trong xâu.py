t = int(input())
while t > 0:
    t-=1
    s = input()
    s1 = input()
    print((len(s) - len(s.replace(s1, ""))) // len(s1))
    # removed = s.replace(s1,"")
