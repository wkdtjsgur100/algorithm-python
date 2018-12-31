_, k = map(int, input().split())
x = sorted(list(map(int, input().split())))

ans, i = 0, 0

while i < len(x):
    t = x[i]

    while i < len(x) and x[i] - t <= k:
        i += 1

    ans += 1 # build a antenna

    t = x[i-1]
    while i < len(x) and x[i] - t <= k:
        i += 1

print(ans)