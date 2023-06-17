def f(a, b, count):
    if a + b >= 255: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 1, b, count - 1), f(a * 2, b, count - 1), f(a, b + 1, count - 1), f(a, b * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(1, 237 + 1) if f(17, i, 2)])
print('20)', [i for i in range(1, 237 + 1) if not(f(17, i, 1)) and f(17, i, 3)])
print('21)', [i for i in range(1, 237 + 1) if not(f(17, i, 2)) and f(17, i, 4)])