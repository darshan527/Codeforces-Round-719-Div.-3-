def rn(n):
    res = int((n - 9 * ((n - 1) // 9)) * (10 ** ((n + 8) // 9) - 1) / 9)
    return res


for _ in range(int(input())):
    n = int(input())
    if n < 10:
        print(n)
        continue
    c = 0
    res = 0
    while True:
        res = rn(c)
        # print(res)
        if res <= n:
            c += 1
        else:
            break
    print(c)
