A, B, C = map(int, input().split())

def go(A, B, C):
    if B == 1:
        return A % C
    if B == 0:
        return 1

    if B % 2 == 0:
        tmp = go(A, B//2, C)
        return tmp*tmp % C
    else:
        return (A * go(A, B-1, C)) % C

print(go(A, B, C))
