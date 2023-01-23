from sys import *
from functools import *
setrecursionlimit(1000000)

@lru_cache(None)
def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        if int(str(start)[-1]) <= 1:
            return f(start + 5, end) + f(start + 10, end)
        else:
            return f(start + 5, end) + f(start + 10, end) + f(start * int(str(start)[-1]), end)
print(f(10, 220))