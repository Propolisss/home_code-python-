

def f(n):
    num = n ** 2
    if n > 1:
        num += 2 * n + 1
        num += f(n - 2) + f(n // 3)
    return num
print(f(100))