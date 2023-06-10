from itertools import *

def f(x, y, w, z):
    return ((x == z) or (x != w)) and ((y <= x) or (not z))

for a in product([0, 1], repeat=9):
    table = [(1, a[0], 1, 1), (a[1], 1, a[2], 1), (a[3], 1, 1, 1), (1, a[4], 1, a[5]), (a[6], 1, a[7], a[8])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0, 0, 0]:
                print(*p, sep='')