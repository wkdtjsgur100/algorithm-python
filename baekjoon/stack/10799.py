stick_cnt = 0
ans = 0
laser = False

# 풀이 1
# ( 은 막대의 시작을 의미하거나, 레이저의 시작을 의미한다.
# ) 은 막대의 끝을 의미하거나, 레이저의 끝을 의미한다.
# ()가 오면 레이저를 의미한다. 즉, 바로 이전에 (가 오고 그 다음에 )가 오면 레이저고, 그 이외의 경우엔 다 막대다.

# 풀이 2
# (가 들어갈 때 index를 스택에 넣어주고 )를 발견했을 시 스택의 가장 위의 index를 확인한다.
# 거리가 1 차이나면 laser, 아니면 막대이다.

for c in input():
    if c == '(':
        if laser: # 막대의 시작일 경우
            stick_cnt += 1
        else: # 레이저의 시작일 경우
            laser = True
    else:
        if laser: # 레이저의 끝일 경우
            ans += stick_cnt
            laser = False
        else: # 막대의 끝일 경우
            stick_cnt -= 1
            ans += 1
print(ans)