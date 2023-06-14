def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(81234, 134689 + 1):
    dels = div(i)
    if len(dels) == 3:
        print(*dels)