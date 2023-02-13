from itertools import *

def f(x, y, w, z):
    return x or ((not y) or z or w) and (y or (not w))

table = [(0, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 0)]

for p in permutations('xywz'):
    if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
        print(*p, sep='')