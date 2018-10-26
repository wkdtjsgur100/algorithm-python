from collections import deque
import sys

left = list(input())
right = deque()
read=lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    inp = read().split()
    cmd = inp[0]

    if cmd == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd == 'D':
        if right:
            left.append(right.popleft())
    elif cmd == 'B':
        if left:
            left.pop()
    elif cmd == 'P':
        left.append(inp[1])

print(''.join(left),end='')
print(''.join(right))
