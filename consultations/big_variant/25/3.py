def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(452021 + 1 + 1, 1_000_000):
    dels = div(i)
    if len(dels) == 0:
        m = 0
    else:
        m = dels[0] + dels[-1]
    if m % 7 == 3:
        print(i, m)
        count += 1
    if count == 5:
        break