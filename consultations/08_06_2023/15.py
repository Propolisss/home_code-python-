from itertools import *

def f(x):
    b = 20 <= x <= 80
    a = a1 <= x <= a2
    return b <= ((x % 17 == 0) <= a)

ox = [i / 4 for i in range(19 * 4, 81 * 4 + 1)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        lens.append(a2 - a1)
print(min(lens))