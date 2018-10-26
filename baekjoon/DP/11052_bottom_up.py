N = int(input())
cards = list(map(int, input().split()))

D = [0]*(N+1)

for i in range(1, N+1):
    for j in range(i):
        D[i] = max(D[i], D[i-j-1] + cards[j])

print(D[N])
