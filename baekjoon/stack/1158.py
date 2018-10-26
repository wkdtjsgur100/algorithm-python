from collections import deque

N, M = map(int, input().split())

deq = deque(range(1, N+1))
ans = []

while deq:
    for _ in range((M-1) % len(deq)):
        deq.append(deq.popleft())
    ans.append(str(deq.popleft()))

print('<%s>' % ', '.join(ans))