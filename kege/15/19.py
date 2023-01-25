from itertools import *

def f(x):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

m = []
ox = [i / 4 for i in range(16 * 4, 84 * 4)]

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m))