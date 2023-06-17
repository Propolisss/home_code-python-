def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(190201, 190260 + 1):
    dels = div(i)
    ch = [j for j in dels if j % 2 == 0]
    if len(ch) == 4:
        print(ch[-1], ch[-2])