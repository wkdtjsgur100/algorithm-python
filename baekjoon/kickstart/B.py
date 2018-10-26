for T in range(int(input())):
    N, Q = map(int, input().split())

    X = [0]*400000
    Y = [0]*400000
    Z = [0]*100000

    X[0], X[1], A1, B1, C1, M1 = map(int, input().split())
    Y[0], Y[1], A2, B2, C2, M2 = map(int, input().split())
    Z[0], Z[1], A3, B3, C3, M3 = map(int, input().split())

    for i in range(2, N):
        X[i] = (A1*X[i-1] + B1*X[i-2] + C1) % M1
        Y[i] = (A2*Y[i-1] + B2*Y[i-2] + C2) % M2

    for i in range(2, Q):
        Z[i] = (A3*Z[i-1] + B3*Z[i-2] + C3) % M3

    L = [min(X[i], Y[i]) + 1 for i in range(N)]
    R = [max(X[i], Y[i]) + 1 for i in range(N)]
    K = [Z[i]+1 for i in range(Q)]

    combined = []
    for l, r in zip(L, R):
        combined.extend(list(range(l, r+1)))

    ans = 0
    combined.sort(reverse=True)

    for i, k in enumerate(K):
        ans += combined[k-1]*(i+1)

    print("Case #%d: %d" % (T+1, ans))

