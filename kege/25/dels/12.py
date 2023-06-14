def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(550_000, 1_000_000):
    dels = div(i)
    s = [j for j in dels if j % 10 == 7]
    if len(s) == 3:
        print(i, s[-1])
        count += 1
    if count == 5:
        break