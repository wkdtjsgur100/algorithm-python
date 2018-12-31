min, max = map(int, input().split())
filter = [True]*(max-min+1)

i = 2
while i*i <= max:
    st = i*i - (min % (i*i))
    if st == i*i:
        st = 0

    j = st
    while j <= max - min:
        filter[j] = False
        j += i*i

    i += 1

print(filter.count(True))
