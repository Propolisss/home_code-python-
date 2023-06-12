from itertools import *

def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for a in product([0, 1], repeat=7):
    table = [(1, 0, a[0], a[1]), (a[2], 1, 0, a[3]), (0, a[4], a[5], a[6])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(*p, sep='')