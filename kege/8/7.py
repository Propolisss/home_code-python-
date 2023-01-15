from itertools import *

count = 0
sogl = 'БКЛН'
gl = 'АИОУ'
for i in permutations('АБИКОЛУН', 8):
    s = ''.join(i)
    if all((s[j] in sogl and s[j - 1] not in sogl) or (s[j] in gl and s[j - 1] not in gl) for j in range(7)):
        count += 1
print(count)