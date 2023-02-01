def f(x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100)

for a in range(1, 3_000):
    if all(f(x) for x in range(1, 30000)):
        print(a)
        break