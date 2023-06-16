def f(x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & a != 0)


for a in range(10000):
    if all(f(x) == 1 for x in range(10000)):
        print(a)
        break