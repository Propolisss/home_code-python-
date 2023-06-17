def f(a, b, count):
    if a + b >= 30: return count % 2 == 0
    if count == 0: return 0
    h = [f(a + 1, b, count - 1), f(a * 2, b, count - 1), f(a, b + 1, count - 1), f(a, b * 2, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

count = 0

for k in range(1, 29 + 1):
    for s in range(1, 29 + 1):
        if f(k, s, 2) and (s + k) < 30:
            count += 1
print(count)