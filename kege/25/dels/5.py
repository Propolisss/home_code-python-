def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(250200, 1_000_000):
    dels = div(i)
    if len(dels) >= 2 and (dels[-1] + dels[0]) % 123 == 17:
        print(i, dels[-1] + dels[0])
        count += 1
    if count == 5:
        break