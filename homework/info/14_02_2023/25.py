def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0

for i in range(800000, 1_000_000_000):
    if count == 6:
        break
    dels = div(i)
    if len(dels) > 10:
        prod = 1
        for i in dels: prod *= i
        if sum(dels) & 1 and prod & 1:
            print(i, len(dels))
            count += 1