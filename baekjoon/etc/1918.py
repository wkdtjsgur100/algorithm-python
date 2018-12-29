stack = [] # 우선 순위 순서대로 연산자가 들어감. 가장 위에 우선순위가 높은 연사자가 있음.
result = [] # 후위 연산 결과. 가장 우선순위가 높은 연산자를 먼저 push해야 함.

op = {'*': 50, '/': 50, '-': 20, '+': 20, '(': 0, ')': 0}

for c in input():
    if c not in op:
        result.append(c)
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and op[stack[-1]] >= op[c]:
            result.append(stack.pop())
        stack.append(c)

while stack:
    result.append(stack.pop())

print(''.join(result))

