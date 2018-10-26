for _ in range(int(input())):
    N = int(input())
    visit = [False]*N
    P = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if not visit[i]:
            go = i
            while not visit[go]:
                visit[go] = True
                go = P[go]-1
            ans += 1

    print(ans)