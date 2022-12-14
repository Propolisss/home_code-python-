from itertools import *

def alpha(st_):
    for i in range(1, len(st_)):
        if (st_[i - 1] in 'ЕЯ' and st_[i] in 'ЕЯ') or (st_[i - 1] in 'ЛС' and st_[i] in 'ЛС'):
            return False
    return True

s = list(map(''.join, product('ЛЕСЯ ', repeat=5)))

count = 0

for i in s:
    if i.count(' ') == 1:
        st = i.split(' ')
        if all(len(j) > 0 for j in st):
            if alpha(i):
                count += 1
print(count)