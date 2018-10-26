import sys

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
group = [[0]*N for _ in range(N)]

sys.setrecursionlimit(1000000)
def go(i, j, group_num):
    group[i][j] = group_num

    s = countries[i][j]
    n = 1

    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for d in direction:
        di = i + d[0]
        dj = j + d[1]

        if 0 <= di < N and 0 <= dj < N and group[di][dj] == 0:
            if L <= abs(countries[i][j] - countries[di][dj]) <= R:
                ts, tn = go(di, dj, group_num)
                s += ts
                n += tn

    return s, n

def unify(i, j, group_num, mean):
    countries[i][j] = mean

    if i+1 < N and group[i+1][j] == group_num:
        unify(i+1, j, group_num, mean)
    if j+1 < N and group[i][j+1] == group_num:
        unify(i, j+1, group_num, mean)

    group[i][j] = 0

cnt = 0
while True:
    means = []
    group_num = 1
    for i in range(N):
        for j in range(N):
            if group[i][j] == 0:
                s, n = go(i, j, group_num)
                means.append(s//n)

                group_num += 1

    if group_num-1 == N*N:
        break

    cnt += 1

    for i in range(N):
        for j in range(N):
            if group[i][j] != 0:
                unify(i, j, group[i][j], means[group[i][j]-1])

print(cnt)