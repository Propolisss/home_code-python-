from itertools import *

count = 0

for i in permutations('ВАЙФУ', 4):
    s = ''.join(i)
    if s[0] != 'Й' and all(j not in s for j in ['ВФ', 'ФВ']):
        count += 1
print(count)