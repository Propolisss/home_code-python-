from fnmatch import *

for i in range(237, 10 ** 8, 237):
    if fnmatch(str(i), '81?2*80') and not(fnmatch(str(i), '*9*')):
        print(i, i // 237)