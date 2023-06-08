from functools import *
from sys import *
setrecursionlimit(10000000)
@lru_cache(None)
def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

@lru_cache(None)
def f(n):
    if n >= 2000:
        return fac(n)
    elif 1 <= n < 2000:
        return 2 * f(n + 1) // (n + 1)

for i in range(5100): fac(i)
for i in range(10): f(i)
print(1000 * f(7) // f(4))