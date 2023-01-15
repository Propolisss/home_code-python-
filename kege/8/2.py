from itertools import *

count = 0

for i in product('ABCWXYZ', repeat=6):
    s = ''.join(i)
    if s[0] in 'WXYZ' and s[-1] in 'WXYZ' and all(s[j] in 'ABC' for j in range(1, 5)):
        count += 1
print(count)