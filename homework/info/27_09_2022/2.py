from itertools import *

s = list(product('АВСХ', repeat=5))
ss = set()


for i in range(len(s)):
    if (s[i][-1] == 'Х' and s[i].count('Х') == 1) or (s[i].count('Х') == 0):
        ss.add(s[i])
print(len(ss))