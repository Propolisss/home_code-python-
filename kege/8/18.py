from itertools import *

count = 0
k = 0

for i in product('АГИЛМОРТ', repeat=4):
    k += 1
    s = ''.join(i)
    if s.endswith('ИМ'):
        count = k
print(count)