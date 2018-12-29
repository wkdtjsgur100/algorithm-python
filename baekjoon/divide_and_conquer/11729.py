def hanoi(fm, to, n):
    if n == 0: return
    hanoi(fm, 6-fm-to, n-1)
    print(fm, to)
    hanoi(6-fm-to, to, n-1)
N=int(input())
print((1<<N)-1)
hanoi(1, 3, N)