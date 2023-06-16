from sys import *
from functools import *
setrecursionlimit(1_000_000)

@lru_cache(None)
def f(n):
    if n <= 4:
        return 1
    if n > 4:
        return f(n - 1) + f(n - 3) + g(n - 2)

@lru_cache(None)
def g(n):
    if n > 1500:
        return 5
    if n <= 1500:
        return g(n + 1) + g(n + 2) + 1

for i in range(1500): g(i)
print((f(1200) + g(100)) % 10000)