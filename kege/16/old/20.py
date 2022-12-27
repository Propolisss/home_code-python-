from functools import lru_cache


@lru_cache
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and (n % 2 == 0):
        return f(n - 2) + n - 2
    if n >= 3 and (n & 1):
        return f(n + 2) + n - 2

count = 0
for i in range(1, 10_000):
    try:
        if len(str(f(i))) == 5:
            count += 1
    except:
        ...
print(count)