def f(n):
    if (n ** 0.5).is_integer():
        return n ** 0.5
    return f(n + 1) + 1

print(f(4850) + f(5000))