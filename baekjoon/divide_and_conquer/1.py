def maxStreak(m, data):
    ans = 0
    acum = 0
    for d in data:
        for flag in d:
            if flag == 'N':
                acum = 0
                break
        else: # 다 Y인 경우
            acum += 1
        if acum > ans:
            ans = acum

    return ans

print(maxStreak(3, ['YNN','YYY','YNN', 'YYY','YYY']))
