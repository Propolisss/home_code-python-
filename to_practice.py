from itertools import *

s1 = list(map(''.join, product('CONST', repeat=5)))
print(len(s1))
