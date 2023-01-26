def f(x, y):
    return (7 * y + x < a) or (2 * x + 3 * y > 98)

for a in range(1_000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break