def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(550000, 1_000_000):
    dels = div(i)
    f = sum(dels) // len(dels) if len(dels) > 0 else 0
    if f % 31 == 13:
        print(i, f)
        count += 1
    if count == 5:
        break