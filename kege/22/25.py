def div(n):
    dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                dels.add(i)
            if (n // i) % 2 == 0:
                dels.add(n // i)
        if len(dels) > 3:
            return [0]
    return sorted(dels)

for i in range(113_000_000, 114_000_000 + 1, 2):
    dels = div(i)
    if len(dels) == 3:
        print(i, dels[-2])