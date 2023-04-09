from itertools import *

def f(x):
    b = 18 <= x <= 52
    c = 16 <= x <= 41
    a = a1 <= x <= a2
    return (b <= a) and ((not c) or a)

ox = [i / 4 for i in range(15 * 4, 53 * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        lens.append(abs(a2 - a1))
print(min(lens))