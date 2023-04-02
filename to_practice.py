from itertools import *

nums = [10 ** i for i in range(8)]

for a in combinations(nums, 3):
    if max(a) ** 2 == min(a) ** 2 + sorted(a)[1] ** 2:
        print(a)