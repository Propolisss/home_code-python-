from itertools import *

count = 0

for i in product('ВИШНЯ', repeat=6):
    s = ''.join(i)
    if s.count('В') <= 1:
        if s[0] != 'Ш' and s[-1] not in 'ИЯ':
            count += 1
print(count)