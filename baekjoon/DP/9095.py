for _ in range(int(input())):
    n = int(input())
    def go(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        return go(n-1) + go(n-2) + go(n-3)

    print(go(n))
