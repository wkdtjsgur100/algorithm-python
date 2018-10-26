# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    go = A[0]
    result = 1

    while go != -1:
        if result < A[go]:
            result = A[go]
        go = A[go]

    return result

print(solution([1, 4, -1, 3, 2]))