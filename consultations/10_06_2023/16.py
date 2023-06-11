from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 3456:
        return n + 1
    elif n <= 3456 and n % 3 == 0:
        return f(n + 1) + f(n + 2)
    elif n <= 3456 and n % 3 != 0:
        return f(n + (n % 3)) + 2

for i in range(5000, -1, -1): f(i)
print(f(12) - f(17))