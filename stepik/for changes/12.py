from fnmatch import *

ans = []

def div(n):
    dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels |= {i, n // i}
    return sum(dels)

count = 0

for i in range(16606, 1_000_000):
    if fnmatch(str(i), '?6*6*?6') and (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0):
        print(i, div(i))
        count += 1
    if count == 7:
        break

