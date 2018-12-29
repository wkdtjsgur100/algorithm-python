import sys

read = lambda: sys.stdin.readline().strip()
for T in range(int(read())):
    N, P = map(int, read().split())
    result = (1 << N)

    mem = []
    top = sys.maxsize

    for _ in range(P):
        su = 0
        for i, c in enumerate(read()):
            su += (1 if c == 'B' else 0) << i

        if top > su:
            top = su
            mem.append(su)

    print(mem)
    print("Case #%d: %d" % (T+1, result))
