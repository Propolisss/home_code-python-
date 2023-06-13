def f(a, b, count):
    if a + b >= 77: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 1, b, count - 1), f(a * 2, b, count - 1), f(a, b + 1, count - 1), f(a, b * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(1, 69 + 1) if f(7, i, 2)])
print('20)', [i for i in range(1, 69 + 1) if f(7, i, 3) and not(f(7, i, 1))])
print('21)', [i for i in range(1, 69 + 1) if f(7, i, 4) and not(f(7, i, 2))])