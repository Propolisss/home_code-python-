from itertools import *
def f(x, y, z, w):
    return ((not x) and y) or (z and (not y)) or ((not z) and w)

for a in product([0, 1], repeat=6):
    table = [(1, 0, a[0], a[1]), (a[2], 1, 0, a[3]), (a[4], a[5], 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
                print(*p, sep='')