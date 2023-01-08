from itertools import *

gl = 'ИОЯА'
s = list(map(''.join, product('ПИТОНЯГА', repeat=8)))
comb = set(map(''.join, product(gl, repeat=2)))
count = 0

for i in s:
    if (i[0] not in gl) and all(j not in i for j in comb):
        count += 1
print(count, len(s))
