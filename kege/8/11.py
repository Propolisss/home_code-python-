from itertools import *

count = 0

for i in set(product('ABCD', repeat=4)):
    s = ''.join(i)
    if all(s[j] <= s[j + 1] for j in range(3)):
        count += 1
print(count)