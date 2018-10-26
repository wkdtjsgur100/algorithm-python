m = [[False]*100 for _ in range(100)]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    dragons = [direction[d]]
    


