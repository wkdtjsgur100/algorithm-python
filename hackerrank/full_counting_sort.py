N = int(input())

sorted = [[] for i in range(100)]
for _ in range(N//2):
    si, s = input().split()
    sorted[int(si)].append('-')

for _ in range(N//2):
    si, s = input().split()
    sorted[int(si)].append(s)

for l in sorted:
    for item in l:
        print(item, end=' ')
