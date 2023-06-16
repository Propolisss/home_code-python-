from sys import *
from functools import *
setrecursionlimit(1_000_000)


@lru_cache(None)
def f(n):

    if n <= 2:
        return (2, 1)
    if n > 2:
        return (f(n - 1)[0] - 2 * f(n - 2)[0], f(n - 1)[1] + f(n - 2)[1] + 1)
print(f(57))