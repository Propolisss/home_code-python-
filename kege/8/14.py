from itertools import *

count = 0

for i in permutations('ДЕЙКСТРА', 6):
    s = ''.join(i)
    if s.count('Й') == 1 and ((s.find('Й') + 1) != 6) and s[s.find('Й') + 1] in 'ДКСТР':
        count += 1
print(count)