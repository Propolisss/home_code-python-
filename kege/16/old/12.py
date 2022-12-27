cache = {}

def f(n):
    if n not in cache:
        if n == 0:
            cache[n] = 1
        if n == 1:
            cache[n] = 3
        if n > 1:
            cache[n] = f(n - 1) - f(n - 2) + 3 * n
    return cache[n]
print(f(40))