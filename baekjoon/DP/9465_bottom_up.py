for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    D = [[0]*N for _ in range(2)]

    D[0][0] = stickers[0][0]
    D[1][0] = stickers[1][0]

    for i in range(1, N):
        D[0][i] = max(D[1][i-1], D[1][i-2] if i-2 >= 0 else 0) + stickers[0][i]
        D[1][i] = max(D[0][i-1], D[0][i-2] if i-2 >= 0 else 0) + stickers[1][i]

    print(max(D[0][N-1], D[1][N-1]))

