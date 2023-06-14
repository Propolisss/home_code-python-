from fnmatch import *

def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)
count = 0
for i in range(65000, 100_000_000):
    if fnmatch(str(i), '6*97*5?'):
        dels = [j for j in div(i) if j % 2 == 0]
        if len(dels) >= 4:
            print(i, sum(dels))
            count += 1
    if count == 7:
        break