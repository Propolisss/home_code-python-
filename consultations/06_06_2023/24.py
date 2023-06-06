from fnmatch import *

st = open('24-230.txt').readline().split('KK')
nums = []
for i in st[1:-1]:
    if i.isdigit() and len(i) > 0:
        nums.append(int(i))
maxx = max(nums)

prod = 1
for i in str(maxx): prod *= int(i) if int(i) & 1 else 1
print(prod)