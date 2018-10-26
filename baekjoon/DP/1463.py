N = int(input())
D = [0]*(N+1)

D[1] = 0
for i in range(2, N+1):
    m = D[i-1]
    if i % 2 == 0:
        m = min(m, D[i//2])
    if i % 3 == 0:
        m = min(m, D[i//3])
    D[i] = m + 1

print(D[N])

