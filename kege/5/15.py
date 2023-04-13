from itertools import *

for i in range(100, 999 + 1):
    maxx = float('-inf')
    minn = float('inf')
    for p in permutations(str(i), 2):
        if ''.join(p)[0] != '0':
            minn = min(minn, int(''.join(p)))
            maxx = max(maxx, int(''.join(p)))
    if abs(maxx - minn) == 5:
        print(i)
        break