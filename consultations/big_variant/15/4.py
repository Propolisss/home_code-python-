def f(x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100)

for a in range(1, 100_00):
    if all(f(x) for x in range(1, 1_000_000)):
        print(a)
        break