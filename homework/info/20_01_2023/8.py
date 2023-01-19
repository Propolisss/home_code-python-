from itertools import *

s = list(map(''.join, product('АКЛОШ', repeat=5)))
count = 0

for i in s:
    if any(gl in i for gl in 'ОА'):
        count += 1
print(count)