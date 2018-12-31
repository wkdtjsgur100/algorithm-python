_, k = map(int, input().split())
arr = set(map(int, input().split()))

ans = 0
for item in arr:
    if item + k in arr:
        ans += 1

print(ans)
