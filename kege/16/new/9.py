from sys import *
from functools import *

setrecursionlimit(1_000_000)

@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2 * f(n - 1)

for i in range(1, 1900 + 1):
    f(i)

print(f(1900) / 2 ** 1890)