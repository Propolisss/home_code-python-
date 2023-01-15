from itertools import *

count = 0

for i in product('ПУЛЯ', repeat=6):
    s = ''.join(i)
    if s.count('У') == 2:
        count += 1
print(count)