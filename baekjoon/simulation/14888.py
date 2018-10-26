N = int(input())
A = list(map(int, input().split()))
op_counts = list(map(int, input().split()))


def division(x, y):
    result = abs(x) // y
    return result if x >= 0 else -result

cal = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: division
}


def go(i, op_counts, s):
    if i+1 >= N:
        return s, s

    global A, cal

    mx = -1000000001
    mn = 1000000001

    for j, op_count in enumerate(op_counts):
        if op_count != 0:
            op_counts[j] -= 1
            mx_cmp, mn_cmp = go(i+1, op_counts, cal[j](s, A[i+1]))
            mx = max(mx, mx_cmp)
            mn = min(mn, mn_cmp)
            op_counts[j] += 1

    return mx, mn

mx, mn = go(0, op_counts, A[0])

print(mx)
print(mn)