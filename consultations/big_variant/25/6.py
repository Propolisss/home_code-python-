def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(460_000_000 + 1, 460_000_000 + 1_000_000):
    dels = div(i)
    if len(dels) >= 5:
        m = dels[-5]
    else:
        m = 0
    if m > 0:
        print(m)
        count += 1
    if count == 5:
        break