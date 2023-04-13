

for n in range(1, 1_000):
    for m in range(1, 1_000):
        p1 = 1
        for i in (str(n) + str(m)):
            p1 *= int(i) if i != '0' and int(i) % 2 == 0 else 1
        p2 = 1
        for i in (str(n) + str(m)):
            p2 *= int(i) if int(i) & 1 else 1
        if n == 120 and abs(p1 - p2)== 29:
            print(n, m)