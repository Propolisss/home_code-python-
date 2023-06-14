def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(400_000_000, 400_000_000 + 1_000_000):
    #print(i)
    dels = div(i)
    p = dels[0] * dels[1] * dels[2] * dels[3] * dels[4] if len(dels) >= 5 else 0
    if p % 100 == 17 and p <= i:
        print(p, dels[4])
        count += 1
    if count == 5:
        break