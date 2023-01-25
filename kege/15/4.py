def f(x):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)

for a in range(1, 3_000):
    if all(f(x) for x in range(10_000)):
        print(a)
        break