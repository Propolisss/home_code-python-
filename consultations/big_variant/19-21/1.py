def f(start, count):
    if start >= 55: return count % 2 == 0
    if count == 0: return 0
    h = [f(start + 1, count - 1), f(start + 4, count - 1), f(start * 3, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(1, 54 + 1) if f(i, 2)])
print('20)', [i for i in range(1, 54 + 1) if not(f(i, 1)) and f(i, 3)])
print('21)', [i for i in range(1, 54 + 1) if not(f(i, 2)) and f(i, 4)])
