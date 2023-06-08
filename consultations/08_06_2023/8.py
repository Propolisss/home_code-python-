from itertools import *

count = 0

for i in product('СМОКАТ', repeat=7):
    s = ''.join(i)
    if (s.find('САМ') not in [0, 4]) and s.count('САМ') == 1 and s[s.find('САМ') - 1] == s[s.find('САМ') + 3] and s[s.find('САМ') - 1] in 'ОА':
        count += 1
print(count)