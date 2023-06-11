from functools import lru_cache


@lru_cache(None)
def f(start, end, count):
    if start > end:
        return 0
    elif start == end:
        return count == 1
    else:
        return f(start + 1, end, count + ((start + 1) & 1)) + f(start + 2, end, count + ((start + 2) & 1)) + f(start * 2, end, count + ((start * 2) & 1))
print(f(2, 40, 0))