def f(a, count, target):
    if a >= 129: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(a + 1, count + 1, target), f(a * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

for i in range(1, 128 + 1):
    if f(i, 0, 4):
        print(i)