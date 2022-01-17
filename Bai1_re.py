def cacl(num):
    ce = 2
    res = [2]
    while num > 1:
        while num % ce == 0:
            num //= ce
            res.append(num)
            res.append(ce)
        ce+=1
    return res


def main():
    print(cacl(220))
    a = list(set(cacl(220)))
    print(sum(a))
main()