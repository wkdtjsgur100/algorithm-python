import copy, sys
cctv=[
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [0, 2], [2, 1], [1, 3]],
    [[1, 2, 3], [0, 1, 2], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

cctv_poses = []

for i in range(len(m)):
    for j in range(len(m[0])):
        if 1 <= m[i][j] <= 5:
            cctv_poses.append((i, j, m[i][j]))

def observe(m, i, j, d):
    if 0 <= i < N and 0 <= j < M and m[i][j] != 6:
        if m[i][j] == 0:
            m[i][j] = -1
        observe(m, i+d[0], j+d[1], d)

def simulate(m, cctv_i):
    global N, M
    if cctv_i == len(cctv_poses):
        return sum(r.count(0) for r in m)

    i = cctv_poses[cctv_i][0]
    j = cctv_poses[cctv_i][1]
    cam_num = cctv_poses[cctv_i][2]
    temp_m = copy.deepcopy(m)

    ret = sys.maxsize
    for sight in range(len(cctv[cam_num-1])):
        for d_num in cctv[cam_num-1][sight]:
            observe(m, i, j, d[d_num])
        ret = min(ret, simulate(m, cctv_i+1))
        m = copy.deepcopy(temp_m)

    return ret

print(simulate(m, 0))
