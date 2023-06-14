from fnmatch import *

def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)
count = 0
for i in range(168, 10 ** 10, 168):
    if fnmatch(str(i), '?6*6*?6'):
        print(i, sum(div(i)))
        count += 1
    if count == 7:
        break