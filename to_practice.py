from itertools import *

def f(x, y, z, w):
    return (x <= y) or (not(w <= z))

table = [(1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 1, 1)]
if len(table) == len(set(table)):
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(*p, sep='')