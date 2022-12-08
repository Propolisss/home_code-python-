def f(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return 3 * f(n - 1) - f(n - 2)
print(f(6))