t =  int(input())
user = []
while t  > 0:
    t-=1
    user.append(input().lower())
res = list(set(user))
for i in res:
    print(i)