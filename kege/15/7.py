def f(x):
    return (( (x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))

for a in range(1, 3_000):
    if all(f(x) for x in range(1, 20_000)):
        print(a)
