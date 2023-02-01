from functools import *
from sys import *
setrecursionlimit(1000000)



@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

for i in range(1, 2025):
    f(i)

print(f(2023) // f(2020))