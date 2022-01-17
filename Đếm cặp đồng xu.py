n = int(input())
a = []
for i in range(n):
    tmp = input()
    a.append(tmp)
res = 0
for i in a:
    count = i.count('C') - 1
    res+=(count*(count+1))/2
    # print(res,count)

for i in range(n):
    count = 0
    for j in range(n):
        if a[j][i] == 'C':
            count+=1
    count-=1
    res+=(count*(count+1))/2
print(int(res))
"""
C4
CC..
C..C
.CC.
.CC.
C
C
C
C
C
C
C
C
C
"""