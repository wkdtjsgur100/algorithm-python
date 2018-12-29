from collections import defaultdict
input()
h = defaultdict(lambda: 0)
for i in input().split():
    h[i] += 1
input()
ans = []
for i in input().split():
    ans.append(str(h[i]) if i in h else '0')

print(' '.join(ans))
