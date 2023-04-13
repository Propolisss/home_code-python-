from itertools import *
count = 0

for i in range(300, 400 + 1):
    maxx = float('-inf')
    minn = float('inf')

    for p in permutations(str(i), 2):
        if ''.join(p)[0] != '0':
            maxx = max(maxx, int(''.join(p)))
            minn = min(minn, int(''.join(p)))
    if maxx - minn == 20:
        count += 1
print(count)