from itertools import *

s = list(map(''.join, product('ПИТОН', repeat=4)))
count = 0
gl = 'ИО'
sogl = 'ПТН'

for i in s:
    if all((i[j] in gl and i[j + 1] in sogl) or (i[j] in sogl and i[j + 1] in gl) for j in range(3)):
        count += 1
print(count)