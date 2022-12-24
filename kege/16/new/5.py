# либо не решается программой, либо не нашел способ
from sys import *
from functools import *

setrecursionlimit(1_000_000)

@lru_cache(None)
def f(n):
    if n >= 1000:
        return n
    if n < 10000 and (n % 3 == 0):
        return n + f(n // 3)
    if n < 10000 and (n % 3 != 0):
        return 2 * n + f(n + 3)

for i in range(10000, -1, -1):
    f(i)

print(f(999) - f(46))