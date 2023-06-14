from fnmatch import *

def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)

for i in range(217, 10 ** 7, 217):
    if fnmatch(str(i), '14?4*'):
        print(i, sum(j for j in div(i) if j & 1))