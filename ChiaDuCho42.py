test = 10
a = ""
while test > 0:
    tmp = input()
    a += tmp
    a+=" "
    test -= len(tmp.split())
b = list(map(int, a.split()))
print(len(set(map(lambda n: n % 42, b))), end="")
