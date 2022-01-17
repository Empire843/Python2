t = int(input())
test = 1
while t > 0:
    t -= 1
    s1 = input()
    s2 = input()
    k = 0
    if len(s1) == len(s2):
        for i in s1:
            if s1.count(i) != s2.count(i):
                k = 1
                print("Test ", test, ":", " NO", sep="")
                break
        if k == 0:
            print("Test ", test, ":", " YES", sep="")

    else:
        print("Test ", test, ":", " NO", sep="")
    test += 1
