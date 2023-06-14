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

for i in range(25317, 51237 + 1):
    dels = div(i)
    s = [j for j in dels if simple(j)]
    if len(s) >= 6:
        print(i, s[-1])