def f(start, count):
    if 36 <= start <= 60: return count % 2 == 0
    if start > 60: return count % 2 != 0
    if count == 0: return 0
    h = [f(start + 1, count - 1), f(start * 2, count - 1), f(start * 3, count - 1)]
    return any(h) if (count - 1) % 2 == 0 else all(h)

for i in range(1, 35 + 1):
    if f(i, 4) and not(f(i, 2)):
        print(i)