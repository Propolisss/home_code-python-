from itertools import *

count = 0

for i in product('ГЕПАРД', repeat=5):
    s = ''.join(i)
    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
        count += 1
print(count)