from functools import lru_cache

pust = ''

@lru_cache
def f(start, end, current, pust):
    previous = pust[:]
    previous += str(current)
    for i in range(1, len(previous)):
        if previous[i - 1] == 3 and previous[i] == 3:
            return 0
    if start > end or start == 28:
        return 0
    if start == end:
        #print(previous)
        previous = previous[:-1]
        return 1
    else:
        f1 = f(start + 1, end, 1, previous)
        f2 = f(start + 3, end, 2, previous)
        f3 = f(start * 2, end, 3, previous)
        return f1 + f2 + f3


print(f(4, 10, 0, pust) * f(10, 93, 0, pust))
