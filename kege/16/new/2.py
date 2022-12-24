from sys import *
from functools import *
#setrecursionlimit(10000)

@lru_cache(None)
def f(n):  
    if n == 1:
        return 1
    if n > 1:
        return n ** 2 + f(n - 1)

for i in range(1, 1000 + 1):
    f(i)

print(f(1000) - f(997))