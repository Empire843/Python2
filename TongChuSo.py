n = input()
if len(n) == 1:
    print(1)
else:
    k = 0
    while len(n) > 1:
        sum = 0
        k += 1
        for i in n:
            if i != '-':
                sum += int(i)
            else:
                sum+=ord('-') - ord('0')
        n = str(sum)
    print(k)
