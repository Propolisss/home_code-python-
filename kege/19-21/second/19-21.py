def f(a, b, c, count):
    if a + b + c >= 73: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 3, b, c, count - 1), f(a + 13, b, c, count - 1), f(a + 23, b, c, count - 1),
         f(a, b + 3, c, count - 1), f(a, b + 13, c, count - 1), f(a, b + 23, c, count - 1),
         f(a, b, c + 3, count - 1), f(a, b, c + 13, count - 1), f(a, b, c + 23, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(1, 23 + 1) if f(2, i, 2 * i, 2)])
print('20)', [i for i in range(1, 23 + 1) if f(2, i, 2 * i, 3) and not(f(2, i, 2 * i, 1))])
print('21)', [i for i in range(1, 23 + 1) if f(2, i, 2 * i, 4) and not(f(2, i, 2 * i, 2))])