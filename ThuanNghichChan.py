    def thuanNghich(n):
        l, r = 0, len(n) - 1
        while l < r:
            if n[l] != n[r]:
                return False
            l += 1
            r -= 1
        return True


    def even(n):
        for i in n:
            if int(i) % 2 != 0:
                return False
        return True


    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(n):
            if (thuanNghich(str(i)) == True) and (even(str(i)) == True) and (len(str(i)) % 2 == 0):
                print(i ," ", end="")
        print()
