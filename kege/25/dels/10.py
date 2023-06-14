def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(500000, 1_000_000):
    dels = div(i)
    n = min(j for j in dels if j != 8 and j % 10 == 8) if len([j for j in dels if j != 8 and j % 10 == 8]) > 0 else 0
    if n > 0:
        print(i, n)
        count += 1
    if count == 5:
        break