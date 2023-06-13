def f(a, b, count):
    if a * b >= 63: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 1, b, count - 1), f(a * 2, b, count - 1), f(a, b + 1, count - 1), f(a, b * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

for i in range(1, 31 + 1):
    if f(2, i, 4) and not(f(2, i, 2)):
        print(i)