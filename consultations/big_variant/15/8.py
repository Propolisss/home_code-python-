from itertools import *

def f(x):
    p = 10 <= x <= 25
    q = 15 <= x <= 30
    r = 25 <= x <= 40
    a = a1 <= x <= a2
    return (q <= (not r)) and a and (not p)

ox = [i / 4 for i in range(9 * 4, 41 * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 0 for x in ox):
        lens.append(a2 - a1)
print(max(lens))