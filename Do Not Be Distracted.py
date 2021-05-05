for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    deltd = set()
    flg = True
    while c < n:
        tmp = s[c]
        if tmp in deltd:
            flg = False
            print("NO")
        if s[c] not in deltd:
            deltd.add(s[c])
        while c < n and s[c] == tmp:
            c += 1
    if flg:
        print("YES")
