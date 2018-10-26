import copy


def move(N, direction, m):
    i_range = range(N)[::-1] if direction[0] > 0 else range(N)
    j_range = range(N)[::-1] if direction[1] > 0 else range(N)

    for i in i_range:
        for j in j_range:
            check_i, check_j = i, j
            t = m[i][j]
            m[i][j] = 0

            while N > check_i >= 0 and N > check_j >= 0:
                if m[check_i][check_j] != 0:
                    if m[check_i][check_j] == t:
                        m[check_i][check_j] += t
                    else:
                        m[check_i-direction[0]][check_j-direction[1]] += t
                    break

                check_i += direction[0]
                check_j += direction[1]
            else:
                m[check_i-direction[0]][check_j-direction[1]] += t

def get_max_tile(m):
    mx = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            mx = max(mx, m[i][j])
    return mx

def simulate(depth, directions, N, _m):
    if depth == 5:
        return get_max_tile(_m)

    mx = 0
    temp_m = copy.deepcopy(_m)
    for d in directions:
        move(N, d, _m)
        mx = max(mx, simulate(depth+1, directions, N, _m))
        _m = copy.deepcopy(temp_m)

    return mx


N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

print(simulate(0, directions, N, m))