def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(350300 + 1, 1_000_000):
    dels = div(i)
    if sum(dels) % 13 == 0 and len(dels) > 0:
        print(i, sum(dels) // 13)
        count += 1
    if count == 6:
        break