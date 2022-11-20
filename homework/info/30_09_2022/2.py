from itertools import *

s = list(map(''.join, product('АБКЛУ', repeat=4)))

for i in range(len(s)):
    flag = 1
    for j in range(len(s[i])):
        if s[i].count(s[i][j]) != 1:
            flag *= 0
    if flag:
        print(s.index(s[i]) + 1)

""" или

print(int('4321', 5) + static)

"""
