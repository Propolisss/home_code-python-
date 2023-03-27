def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)


count = 0

for i in range(250200, 10 ** 20):
    dels = div(i)
    if len(dels) > 0:
        if (dels[0] + dels[-1]) % 123 == 17:
            count += 1
            print(i, dels[0] + dels[-1])
    if count == 5:
        break