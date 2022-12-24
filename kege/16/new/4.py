from sys import *
from functools import *

setrecursionlimit(12000)

@lru_cache(None)
def f(n):
    if n <= 3:
        return n
    if n > 3:
        if n & 1:
            return 2 * n + f(n - 2)
        else:
            return n ** 2 + f(n - 1)

for i in range(1, 10_000 + 1):
    f(i)

print(f(10000) - f(9995))