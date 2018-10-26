def find_pos(ch):
    for i in range(N):
        for j in range(M):
            if m[i][j] == ch:
                return i, j

N, M = map(int ,input().split())
m = [input() for _ in range(N)]

red_pos = find_pos('R')
blue_pos = find_pos('B')






