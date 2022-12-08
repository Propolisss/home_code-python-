def f(a, b, c, count, target):
    if (a + b + c) >= 73: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(a + 3, b, c, count + 1, target), f(a + 13, b, c, count + 1, target), f(a + 23, b, c, count + 1, target), f(a, b + 3, c, count + 1, target), f(a, b + 13, c, count + 1, target), f(a, b + 23, c, count + 1, target), f(a, b, c + 3, count + 1, target), f(a, b, c + 13, count + 1, target),f(a, b, c + 23, count + 1, target)]
    return any(h) if (count + 1) % 2 == (target % 2) else all(h)

for s in range(1, 23 + 1):
    if f(2, s, 2 * s, 0, 4) and (not f(2, s, 2 * s, 0, 3)):
        print(s)