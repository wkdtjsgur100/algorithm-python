N, r, c = map(int, input().split())


def find_z(n, sr, sc, er, ec):
    global r, c
    if sr == er and sc == ec:
        return 0

    mr = (sr + er) >> 1
    mc = (sc + ec) >> 1

    cnt = 1 << ((n-1) << 1)
    if r <= mr:
        if c <= mc:
            return find_z(n-1, sr, sc, mr, mc)
        else:
            return find_z(n-1, sr, mc+1, mr, ec) + cnt
    else:
        if c <= mc:
            return find_z(n-1, mr+1, sc, er, mc) + cnt*2
        else:
            return find_z(n-1, mr+1, mc+1, er, ec) + cnt*3

print(find_z(N, 0, 0, (1<<N)-1, (1<<N)-1))