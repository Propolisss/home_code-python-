from sys import *
from functools import *

@lru_cache(None)
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

setrecursionlimit(1_000_000)

@lru_cache(None)
def f(n):
    if n >= 150:
        return fact(n)
    if 1 <= n < 150:
        return 2 * f(n + 1) / (n + 1)

for i in range(5000 + 1):
    fact(i)

for i in range(1, 7 + 1):
    f(i)

print(1000 * f(7) / f(4))