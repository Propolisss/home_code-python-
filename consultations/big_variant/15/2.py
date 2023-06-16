def f(x, y):
    b = 50 <= x <= 70
    return ((2 * x + y) != 150) or (not b) or (a > y)

for a in range(100000):
    if all(f(x, y) == 1 for x in range(10_000) for y in range(10_000)):
        print(a)
        break