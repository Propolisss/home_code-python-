from itertools import *

count = 0

for i in set(product('AB123', repeat=8)):
    s = ''.join(i)
    if (s.count('A') + s.count('B')) == 2:
        count += 1
print(count)