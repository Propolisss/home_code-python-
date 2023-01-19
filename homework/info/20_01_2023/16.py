from sys import *
from functools import *
setrecursionlimit(10000000)


@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 2 * f(1 - n) + 3 * f(n - 1) + 2
    elif n < 0:
        return -f(-n)


print(sum(int(i) for i in str(f(50))))