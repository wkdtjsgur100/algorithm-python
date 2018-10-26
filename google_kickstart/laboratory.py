from itertools import combinations
import copy

R, C = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R) ]

comb_list=[]
virus_list=[]

for r in range(R):
    for c in range(C):
        if m[r][c] == 0:
            comb_list.append((r, c))
        elif m[r][c] == 2:
            virus_list.append((r, c))

def get_safe_area(m):
    re = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                re += 1
    return re

def spread_virus(m, r, c):
    if m[r][c] == 1:
        return

    m[r][c] = 1
    if 0 <= r-1: spread_virus(m, r-1, c)
    if len(m) > r+1: spread_virus(m, r+1, c)
    if 0 <= c-1: spread_virus(m, r, c-1)
    if len(m[0]) > c+1: spread_virus(m, r, c+1)

ans = 0
for w_t in combinations(comb_list, 3):
    copied_map = copy.deepcopy(m)

    # 벽을 세움
    for r, c in w_t:
        copied_map[r][c] = 1

    # virus 퍼뜨림
    for virus in virus_list:
        spread_virus(copied_map, virus[0], virus[1])

    ans = max(ans, get_safe_area(copied_map))

print(ans)

