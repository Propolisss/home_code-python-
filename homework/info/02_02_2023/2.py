from itertools import *

def f(x, y, w, z):
    return (not(y <= x)) or (z <= w) or (not z)

for a in product([0, 1], repeat=7):
    table = [(a[0], 0, a[1], a[2]), (0, 1, a[3], a[4]), (1, a[5], a[6], 0)]

    for p in permutations('xywz'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(*p, sep='')