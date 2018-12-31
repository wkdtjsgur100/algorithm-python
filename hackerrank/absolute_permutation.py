import sys

def abs_perm(pos, i, k):
    if k == 0:
        return True

    if i >= len(pos):
        return True

    if pos[i] > k and pos[i] - k not in pos[:i]:
        pos[i] -= k
        return abs_perm(pos, i+1, k)
        pos[i] += k

    if pos[i] + k <= len(pos) and pos[i] + k not in pos[:i]:
        pos[i] += k
        return abs_perm(pos, i+1, k)
        pos[i] -= k

    return False

for _ in range(int(input())):
    n, k = map(int, input().split())
    pos1 = list(range(1, n+1))
    sys.setrecursionlimit(100000)

    is_finded = abs_perm(pos1, 0, k)
    print(' '.join(map(str, pos1)) if is_finded else -1)
