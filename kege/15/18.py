from itertools import *

def f(x):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

m = []
ox = [i / 4 for i in range(16 * 4, 81 * 4)]

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m))