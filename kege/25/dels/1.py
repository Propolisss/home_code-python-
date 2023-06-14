def div(n):
    dels_ = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(174457, 174505 + 1):
    dels = div(i)
    if len(dels) == 2:
        print(*dels)