from itertools import combinations

def dijkstra(K, V, graph):
    INF = 10001
    s = [False]*V
    d = [INF]*V
    d[K-1] = 0

    while True:
        m = INF
        N = -1

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j

        if m == INF:
            break

        s[N] = True
        for j in range(V):
            if s[j]: continue

            via = d[N] + graph[N][j]

            if d[j] > via:
                d[j] = via
    return d

for _ in range(int(input())):
    V, E = map(int, input().split())
    inf = 100001
    dist = [[inf]*V for _ in range(V)]
    for k in range(V):
        dist[k][k] = 0

    for i in range(E):
        x, y, w = map(int, input().split())
        dist[x-1][y-1] = dist[y-1][x-1] = w

    min_dist = [[inf]*V for _ in range(V)]
    for i in range(V):
        min_dist[i] = dijkstra(i+1, V, dist)

    ans = 0
    min_ans = inf

    for i in range(V-1):
        mean = 0
        for fruits in combinations(range(V), i+1):
            vegs = []
            for i in range(V):
                if i not in fruits:
                    vegs.append(i)

            min_sum = 0
            for f in fruits:
                m = inf
                for v in vegs:
                    if m > min_dist[f][v]:
                        m = min_dist[f][v]
                min_sum += m
            mean += min_sum

        mean /= V
        if min_ans >= mean:
            min_ans = mean

    print(min_ans)
    print("EOF")






