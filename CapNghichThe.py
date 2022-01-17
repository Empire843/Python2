def solution(a):
    res = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                res += 1

    return res


n = int(input())
a = list(map(int, input().split()))
print(solution(a))
