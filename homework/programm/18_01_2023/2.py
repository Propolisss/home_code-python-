from itertools import *

s = set(map(''.join, product('КОМПЬЮТЕР', repeat=5)))

count = 0

for i in s:
    for j in permutations(i):
        if j == j[::-1]:
            count += 1
            break
print(count)