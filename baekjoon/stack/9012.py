def vaild(s):
    stk = 0

    for c in s:
        if c == '(':
            stk += 1
        else:
            if stk:
                stk -= 1
            else:
                return False
    if stk:
        return False

    return True
for _ in range(int(input())):
    if vaild(input()): print("YES")
    else: print("NO")