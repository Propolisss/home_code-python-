from itertools import *

count = 0

for i in permutations('ИГРОК'):
    s = ''.join(i)
    if s[0] != 'К' and 'РОК' not in s:
        count += 1
print(count)