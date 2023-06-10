
for n in range(1, 1_000):
    for m in range(1, 1_000):
        p1 = 1
        p2 = 1
        for i in str(n) + str(m):
            p1 *= int(i) if i in '2468' else 1
            p2 *= int(i) if i in '13579' else 1
        if abs(p1 - p2) == 29 and n == 120:
            print(m)