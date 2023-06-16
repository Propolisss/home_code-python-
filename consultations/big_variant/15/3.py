from itertools import *

def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    return (not((not p) <= q)) <= (a <= ((not q) <= p))

ox = [i / 4 for i in range(12 * 4, 24 * 4 + 1)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lens.append(a2 - a1)
print(max(lens))