gears = [int(input(), 2) for _ in range(4)]

rotate = {
    1: lambda gear: ((gear & 1) << 7) | (gear >> 1),
    -1: lambda gear: bool(gear & (1 << 7)) | ((gear << 1) & ((1 << 8) - 1))
}

get_contact = {
    0: lambda gear: bool(gear & (1 << 1)),
    1: lambda gear: bool(gear & (1 << 5))
}

v = [False]*4

def rotateGear(g_num, d):
    global gears, rotate, v

    v[g_num] = True
    tmp_gears = gears[g_num]
    gears[g_num] = rotate[d](gears[g_num])

    if g_num + 1 < 4 and not v[g_num+1]:
        if get_contact[1](tmp_gears) != get_contact[0](gears[g_num+1]):
            rotateGear(g_num+1, -d)

    if g_num - 1 >= 0 and not v[g_num-1]:
        if get_contact[0](tmp_gears) != get_contact[1](gears[g_num-1]):
            rotateGear(g_num-1, -d)

def get_scores(gears):
    scores = 0
    for i, gear in enumerate(gears):
        scores += ((gear & (1 << 7)) >> 7) * (2**i)
    return scores

for _ in range(int(input())):
    g_num, d = map(int, input().split())
    rotateGear(g_num-1, d)
    v = [False]*4

print(get_scores(gears))



