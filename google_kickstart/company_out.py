N = int(input())
T = []
P = []

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

def go(i, s):
    global T, P, N
    # N이 되면 s+P[i]을 선택받을 수 있게 된다.
    if i == N:
        return s

    # N을 넘어가면 선택받으면 안된다. 따라서 0을 반환.
    if i > N:
        return 0

    return max(go(i+1, s), go(i+T[i], s+P[i]))

print(go(0, 0))
