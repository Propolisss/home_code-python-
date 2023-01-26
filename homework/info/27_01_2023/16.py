def f(n):
    count = 2 * n + 1
    if n > 1:
        count += 3 * n - 8
        count += f(n - 1)
        count += f(n - 4)
    return count
print(f(50))