from itertools import *

k = 0

for i in product('ЕЛМРУ', repeat=4):
    k += 1
    s = ''.join(i)
    if s[0] == 'Л':
        print(k)
        break