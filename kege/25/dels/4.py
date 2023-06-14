def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)
count = 0

for i in range(150_000, 1_000_000):
    dels = div(i)
    summ = sum(dels)
    if summ % 13 == 10:
        print(i, summ)
        count += 1
    if count == 7:
        break