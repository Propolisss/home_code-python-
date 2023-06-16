from sys import *
from functools import *
setrecursionlimit(1_000_000)

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1) + 1
for i in range(3303): f(i)
print(f(3303) // f(3300))