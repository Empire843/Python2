# import math

# def uocSo(n):
#     res = [1]
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             res.append(i)
#     return res


# t = int(input())
# while t > 0:
#     t-=1
#     count = 0
#     a, b = list(map(int,input().split()))
#     for i in range(a,b+1):
#         s = sum(uocSo(i))
#         if(s >= a and s <= b and sum(uocSo(s)) == i and s != i):
#             count+=1
#             # print(uocSo(s))
#             # print(i,s)
#     print(count//2)
def cacl():
    a = 0
    num = int(input())
    ce = 2
    while num > 1:
        while num % ce == 0:
            a += ce
            num /= ce
        ce += 1
    return a


def ptMain():
    t = int(input())
    p = 1
    for i in range(t):
        p *= cacl()
    print(p)

if __name__ == '__main__':
    ptMain()
    # print(cacl())