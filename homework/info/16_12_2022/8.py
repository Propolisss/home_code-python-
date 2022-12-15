from itertools import *

s1 = list(map(''.join, product('ГОЛ', repeat=10)))
s2 = list(map(''.join, product('ГОЛ', repeat=10)))
count = 0
k = 0
for i in s1:
    k += 1
    print(k)
    for j in s2:
        st = i + j
        if ('ГГ' not in st) and ('ОО' not in st) and ('ЛЛ' not in st) and ('ОГО' not in st) and ('ЛГЛ' not in st) and (st[0] != 'Г') and (st[-1] != 'Г'):
            print(count)
            count += 1
print(count)