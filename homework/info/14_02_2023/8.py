from itertools import *

s = list(map(''.join, product('ИНСТАВК', repeat=4)))
ans = []
for i in range(len(s)):
    if s[i][0] in 'НСТВК' and s[i][-1] in 'ИА':
        ans.append(s[i])
ans.sort()
print(ans.index('НИКА') + 1)