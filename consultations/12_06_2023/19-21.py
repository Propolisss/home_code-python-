def f(start, count):
    if start >= 129: return count % 2 == 0
    if count == 0: return 0
    h = [f(start + 1, count - 1), f(start * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

print('19)', [i for i in range(1, 128 + 1) if f(i, 2)])
print('20)', [i for i in range(1, 128 + 1) if f(i, 3) and not(f(i, 1))])
print('21)', [i for i in range(1, 128 + 1) if f(i, 4) and not(f(i, 2))])