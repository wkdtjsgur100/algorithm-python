from collections import deque

N, M = map(int, input().split())
graph = [0]*(N+1)
ind = [0]*(N+1)
q = deque()
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A] = B
    ind[B] += 1

for i in range(1, N+1):
    if ind[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    ans.append(current)
    ind[graph[current]] -= 1
    if ind[graph[current]] == 0:
        q.append(graph[current])

print(' '.join(map(str, ans)))

