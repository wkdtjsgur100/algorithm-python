N, M = map(int, input().split())
A = input().split()
B = input().split()
i = j = 0

ans = []
while i < N and j < M:
    if int(A[i]) < int(B[j]):
        ans.append(A[i])
        i += 1
    else:
        ans.append(B[j])
        j += 1

while i < N:
    ans.append(A[i])
    i += 1

while j < M:
    ans.append(B[j])
    j += 1

print(' '.join(ans))

