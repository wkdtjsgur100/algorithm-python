A, P = map(int, input().split())
mem = {A: 0}

conv = lambda x: sum(map(lambda y: int(y)**P, str(x)))
D = conv(A)
while D not in mem:
    mem[D] = len(mem)
    D = conv(D)
lim_index = mem[D]
ans = 0
for m in mem:
    if mem[m] < lim_index:
        ans += 1

print(ans)