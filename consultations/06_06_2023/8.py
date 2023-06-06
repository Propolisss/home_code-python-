from itertools import *

count = 0

for i in product('POLYGN', repeat=5):
    s = ''.join(i)
    if s == s[::-1] and s[2] in 'OY':
        count += 1
print(count)