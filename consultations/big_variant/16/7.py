from sys import *
from functools import *
setrecursionlimit(1_000_000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - 2 * g(n - 1)

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + g(n - 1) + n
print(sum(int(i) for i in str(g(36))))