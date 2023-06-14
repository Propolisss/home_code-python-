from fnmatch import *

for i in range(51, 10 ** 6 + 1, 51):
    if fnmatch(str(i), '12*45*'):
        print(i, i // 51)