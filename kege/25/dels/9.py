def div(n):
    dels_ = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(1204300, 1204380 + 1):
    dels = div(i)
    summ = sum(j for j in dels if j % 2 == 0)
    if summ != 0 and summ % 10 == 0:
        print(i, summ)