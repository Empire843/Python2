# def radix_conversion(n, k):
#     res = ""
#     while n >= k:
#         res = str(n % k) + res
#         n //= k
#     res = str(n) + res
#     return res
#
#
# a, b, k = list(map(int, input().split()))
# count = 0
# ans = []
# res = []
# ans = [j for j in range(a, b + 1) if (bin(j)[2:]) == (bin(j)[2:])[::-1]]
# for i in range(3, k + 1):
#     ans = [j for j in ans if radix_conversion(j, i) == radix_conversion(j, i)[::-1]]
#     if len(ans) == 0:
#         break
# print(len(ans))
def radix_conversion(n, k):
    res = ""
    while n >= k:
        res = str(n % k) + res
        n //= k
    res = str(n) + res
    return res


a, b, k = list(map(int, input().split()))
count = 0
ans = []
res = []
for i in range(a, b + 1):
    n = bin(i)[2:]
    if n == n[::-1]:
        ans.append(i)
for i in range(3, k + 1):
    ans = [j for j in ans if radix_conversion(j, i) == radix_conversion(j, i)[::-1]]
    if len(ans) == 0:
        break
print(len(ans))
