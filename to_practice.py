from functools import *
from sys import *
setrecursionlimit(1000000)

@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    else:
        print(f(n - 1), (3 ** (n % 5)), (3 ** (n % 7)))
        return f(n - 1) * (3 ** (n % 5)) / (3 ** (n % 7))

print(f(5))