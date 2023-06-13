from fnmatch import fnmatch

st = open('24-228.txt').readline().split('XX')
maxx = float('-inf')

for i in st:
    if fnmatch(i, '3????78??45'):
        maxx = max(maxx, int(i))
summ = sum(int(i) for i in str(maxx) if i in '13579')
prod = 1
for i in str(maxx):
    if i in '02468':
        prod *= int(i)
print(summ + prod)