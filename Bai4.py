capso = []
def lienKeCungDau(a):
    res = 0
    for i in range(len(a) - 1):
        if (a[i] > 0 and a[i+1] > 0) or ((a[i] < 0 and a[i+1] < 0)):
            res+=1
            capso.append(a[i])
            capso.append(a[i + 1])
    return res

n = int(input())
a = list(map(int,input().split()))
k = lienKeCungDau(a)
if(k != 0):
    print(k, end =" ")
    print(capso[len(capso)-2],capso[len(capso)-1])
else:
    print(0)
