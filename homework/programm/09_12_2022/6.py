from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    elif n > 0 and (n & 1):
        return 1 + f(n - 1)
    else:
        return f(n // 2)
count = 0

for i in range(1, 500_000_000 + 1):
    if f(i) == 3:
        print(i, f(i))
        count += 1
print(count)