from collections import Counter

def deleteProducts(ids, m):
    cnts = Counter(ids)
    print(cnts)
    std_cnts = sorted(cnts.items(), key=lambda t: t[1])
    print(std_cnts)
    i = 0
    while m > 0 and std_cnts:
        if std_cnts[i][1] <= m:
            std_cnts.pop(0)
        m -= std_cnts[i][1]

    return len(std_cnts)

print(deleteProducts([1,2,3], 2))