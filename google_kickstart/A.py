from collections import defaultdict


def anagrams(A, B):
    ans = 0
    for l in range(1, len(A)+1):
        Asub = defaultdict(lambda: 0)
        Bsub = defaultdict(lambda: 0)

        for i in range(len(A) - l + 1):
            Asub[''.join(sorted(A[i:i + l]))] += 1
            Bsub[''.join(sorted(B[i:i + l]))] += 1

        for a in Asub:
            if a in Bsub:
                ans += Asub[a]

    return ans

for t in range(int(input())):
    input()
    print("Case #%d: %d" % (t+1, anagrams(input(), input())))
