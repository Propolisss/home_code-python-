from itertools import *

count = 0

for i in product('КРЕСЛО', repeat=4):
    s = ''.join(i)
    if s[0] in 'КРСЛ' and s[-1] in 'ЕО':
        count += 1
print(count)