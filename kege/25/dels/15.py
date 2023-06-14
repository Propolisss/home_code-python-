def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def div(n):
    dels_ = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

count = 0
for i in range(500_000 -1, -1, -1):
    dels = div(i)
    summ = sum(j for j in dels if simple(j))
    if summ != 0 and summ % 10 == 0:
        print(i, summ)
        count += 1
    if count == 7:
        break