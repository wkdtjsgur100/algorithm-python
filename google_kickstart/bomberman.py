rs, cs, n = map(int, input().split())
grid = [input() for _ in range(rs)]

def switch(c):
    return '.' if c == 'O' else 'O'

if n % 2 == 0:
    grid = [['O']*cs for _ in range(rs)]
elif n <= 1 or (n-1)%4 == 0:
    pass
else:
    new_grid = [['.']*cs for _ in range(rs)]

    for r in range(rs):
        for c in range(cs):
            if grid[r][c] == 'O':
                new_grid[r][c] = 'O'
                if r+1 < rs: new_grid[r+1][c] = 'O'
                if r-1 >= 0: new_grid[r-1][c] = 'O'
                if c+1 < cs: new_grid[r][c+1] = 'O'
                if c-1 >= 0: new_grid[r][c-1] = 'O'

    for r in range(rs):
        grid[r] = list(map(switch, new_grid[r]))

for r in range(rs):
    print(''.join(grid[r]))



