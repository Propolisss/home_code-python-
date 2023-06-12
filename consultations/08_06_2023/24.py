from fnmatch import *

st = open('24-230.txt').readline().split('ZZ')
maxx = float('-inf')

for i in st[1:-1]:
    if i.isdigit() and fnmatch(i, '8???54???22'):
        maxx = max(maxx, int(i))
prod = 1
for i in str(maxx):
    prod *= int(i) if i in '13579' else 1
print(prod)