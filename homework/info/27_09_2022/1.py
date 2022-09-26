from itertools import *

gl = 'ЕЭ'
s = list(product('ЕГЭ', repeat=5))

count = 0

for i in range(len(s)):
    if s[i][0] in gl:
        count += 1
print(count)