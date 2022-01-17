t = int(input())
while t > 0:
    t -= 1
    count = 0
    n = int(input())
    k = 1
    i = 1
    while (2*n-i*(i+1)) >= (2*(i+1)) and (i*(i+1) < 2*n):
        x = (2*n-i*(i+1))/(2*(i+1))
        if x - int(x) == 0.0:
            count+=1
        i+=1
    print(count)
