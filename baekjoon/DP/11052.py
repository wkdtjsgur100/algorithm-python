N = int(input())
cards = list(map(int, input().split()))
D = [0]*(N+1)

def get_max_payment(N):
    global cards
    if N < 0:
        return -987654321

    if N == 0:
        return 0

    if D[N]:
        return D[N]

    mx = 0
    for i in range(1, len(cards)+1):
        mx = max(mx, cards[i-1] + get_max_payment(N-i))

    D[N] = mx
    return mx

print(get_max_payment(N))