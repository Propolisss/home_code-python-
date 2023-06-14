def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(154026, 154043 + 1):
    dels = div(i)
    if len(dels) == 4:
        print(*dels[-2:])