from itertools import *

k = 0

for i in product('АИМРЯ', repeat=4):
    k += 1
    s = ''.join(i)
    if s == 'АРИЯ':
        print(k)
        break