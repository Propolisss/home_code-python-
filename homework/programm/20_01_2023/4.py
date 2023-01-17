from itertools import *

alph = 'qwertyuiopasdfghjklzxcvbnm'
s1 = set(map(''.join, product(alph, repeat=5)))
count = 0

print(26 * len(s1))