from itertools import *

k = 0

for i in product('АИМРЯ', repeat=4):
    k += 1
    if k == 211:
        print(''.join(i))
        break