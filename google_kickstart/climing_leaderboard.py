input()
scores = list(map(int, input().split()))
input()
alice = list(map(int, input().split()))

unique_scores = list(reversed(sorted(set(scores))))

i = len(alice)-1
j = 0
ans = []

while i >= 0:
    if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
        ans.append(j+1)
        i -= 1
    else:
        j += 1

print(ans)