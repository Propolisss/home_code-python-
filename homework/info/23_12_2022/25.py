from fnmatch import *

for i in range(27, 10 ** 8 + 1, 27):
    if fnmatch(str(i), '123*890') and (i % 27 == 0):
        print(i, i // 27)