def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(39345679 -1, -1, -1):
    dels = div(i)
    if i % (2 * 3 * 5 * 7) == 0 and 76 <= len(dels) <= 88:
        print(i, len(dels))
        count += 1
    if count == 10:
        break