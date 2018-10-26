import sys

sys.setrecursionlimit(1000000)
for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    D = [[-1]*N for _ in range(2)]

    def go(r, c):
        global N, stickers
        if c >= N:
            return 0

        if D[r][c] != -1:
            return D[r][c]

        ch_r = 0 if r == 1 else 1
        D[r][c] = max(go(ch_r, c+1), go(ch_r, c+2)) + stickers[r][c]
        return D[r][c]

    print(max(go(0, 0), go(1, 0)))
