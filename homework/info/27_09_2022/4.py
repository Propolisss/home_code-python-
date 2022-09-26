from itertools import *

s = list(product('КРАС', repeat=6))
count = 0

for i in range(len(s)):
    if (s[i].count('К') + s[i].count('Р') + s[i].count('С')) >= 3:
        print(s[i])
        count += 1
print(count)