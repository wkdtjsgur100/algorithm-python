def go(i, ids, workHours, dayHours, pattern):
    if i == len(ids):
        print(''.join(map(str, ids)))
        return

    for j in range(dayHours + 1):
        ids[i] = j
        go(i+1, ids, workHours, dayHours, pattern)




def findSchedules(workHours, dayHours, pattern):
    ids = [i for i, k in enumerate(pattern) if k == '?']
    ids = [0]*(dayHours+1)

    go(0, ids, workHours, dayHours, list(pattern))

print(findSchedules(3, 2, '??2??00')) # 답 4개
