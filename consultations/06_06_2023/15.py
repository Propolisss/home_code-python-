from itertools import *
def f(x):
    b = 10 <= x <= 40
    a = a1 <= x <= a2
    return a or (b <= (x % 6 != 0))

ox = [i / 4 for i in range(100 * 4)]
lens = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        lens.append(a2 - a1)
print(min(lens))