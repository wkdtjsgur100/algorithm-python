from itertools import combinations

def solution(relation):
    ans = 0
    clen = len(relation[0])

    for i in range(clen):
        for t in combinations(range(0, clen), i+1):
            print(t)

    return ans

print(solution([[100,'ryan','music',2],[200,'apeach','math',2],[300,'tube','computer',3],[400,'con','computer',4],[500,'muzi','music',3],[600,'apeach','music',2]]))