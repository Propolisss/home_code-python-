from functools import *

@lru_cache(None)
def summ(n):
    return sum(int(i) for i in str(n))

@lru_cache(None)
def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        return count == 5
    else:
        return f(start + 2, end, count + (summ(start + 2) == 14)) + f(start * 3, end, count + (summ(start * 3) == 14)) + f(start * 4, end, count + (summ(start * 4) == 14))
print(f(1, 600, 0))