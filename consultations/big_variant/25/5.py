from fnmatch import *

for i in range(10 ** 8 + 1):
    if fnmatch(str(i), '124*5*79') and i % sum(int(j) for j in str(i) if int(j) & 1) == 0:
        print(i, sum(int(j) for j in str(i)))