from itertools import *

def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = a1 <= x <= a2
    return (A <= P) or Q

nums = [i / 4 for i in range(11 * 4, 54 * 4)]
ans = []

for a1, a2 in combinations(nums, 2):
    if all(f(x) == 1 for x in nums):
        ans.append(a2 - a1)
print(max(ans))
