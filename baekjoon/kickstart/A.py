for T in range(int(input())):
    n = int(input())
    ans = 0
    l = sorted(list(map(int, input().split())))
    s = {}

    for i, item in enumerate(l):
        for j in range(0, i):
            mod = item % l[j] if l[j] != 0 else 0
            if mod == 0:
                d = (item // l[j]) if l[j] != 0 else 0
                if d in s:
                    if j < s[d]:
                        ans += 1

        s[item] = i

    print("Case #%d: %s" % (T+1, ans))