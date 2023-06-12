from itertools import *
count = 0

for i in product('АНТИУОПЯX', repeat=7):
    s = ''.join(i)
    if s.count('X') == 1 and s[0] not in 'АX' and s[-1] not in 'ЯX':
        count += 1
print(count)