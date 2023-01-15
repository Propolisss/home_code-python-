from itertools import *

count = 0

for i in product('ЛОДКА', repeat=4):
    s = ''.join(i)
    if s.count('О') >= 2:
        count += 1
print(count)