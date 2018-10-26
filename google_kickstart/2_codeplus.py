m = int(input())
limit = list(map(int, input().split()))
initial = list(map(int, input().split()))
press_count = int(input())

result = ''
carry = int(press_count)
for i in range(len(limit))[::-1]:
    lim, init = limit[i], initial[i]

    if int(lim) < int(init):
        print(-1)
        break

    tail = int(initial[i]) + carry % (int(limit[i])+1)
    result = str(tail % (limit[i]+1)) + result
    carry = carry // (limit[i]+1)

    if int(tail) >= (limit[i]+1):
        carry += 1
else:
    print(result)


