n = input()
k = 0
for i in n:
    if int(i) == 4 or int(i) == 7:
        k += 1
if k == 4 or k == 7:
    print("YES")
else:
    print("NO")
