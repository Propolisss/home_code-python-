from fnmatch import *

count = 0

for i in range(700000, 700000 + 1_000_000):
    if i % 13 == 0:
        if not(fnmatch(str(i), '*0??3*')) and not(fnmatch(str(i), '*4??2')) and not(fnmatch(str(i), '*1*')):
            print(i, sum(int(j) for j in str(i)))
            count += 1
    if count == 5:
        break