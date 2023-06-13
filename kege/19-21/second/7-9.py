def f(a, b, count):
    if a + b >= 59: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 1, b, count - 1), f(a * 2, b, count - 1), f(a, b + 1, count - 1), f(a, b * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

for i in range(2, 53):
    if not(f(5, i, 2)) and f(5, i, 4):
        print(i)