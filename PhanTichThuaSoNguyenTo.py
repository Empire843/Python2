t = int(input())
while (t > 0):
    t -= 1
    n = int(input())
    i = 2
    print(1,'*',end = " ")
    while n > 1:
        count = 0
        while n % i == 0:
            n/=i
            count+=1
        if count != 0:
            print(i,"^",count,sep = "",end = " ")
            if n > 1:
                print('*', end = " ")
        i+=1
    print()