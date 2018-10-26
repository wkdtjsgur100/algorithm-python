from itertools import combinations
import sys

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

chicken_poses = []
house_poses = []

for r in range(N):
    for c in range(N):
        if m[r][c] == 1:
            house_poses.append((r,c))
        elif m[r][c] == 2:
            chicken_poses.append((r,c))

ans = sys.maxsize
for chicken_pos in combinations(chicken_poses, M):
    sum_chicken_dist = 0
    # 집과 가장 가까운 치킨집을 찾는다
    for hr, hc in house_poses:
        min_chicken_dist = sys.maxsize
        for r, c in chicken_pos:
            chicken_dist = abs(hr - r) + abs(hc - c)
            if min_chicken_dist > chicken_dist:
                min_chicken_dist = chicken_dist
        sum_chicken_dist += min_chicken_dist
    if ans > sum_chicken_dist:
        ans = sum_chicken_dist

print(ans)