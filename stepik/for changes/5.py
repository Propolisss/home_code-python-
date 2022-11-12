

for n in range(1, 10000):
    for m in range(1, 10000):
        p1n = 1
        p1m = 1
        for i in str(n):
            if int(i) % 2 == 0 and i != '0':
                p1n *= int(i)
        for i in str(m):
            if int(i) % 2 == 0 and i != '0':
                p1m *= int(i)
        p1 = p1n * p1m
        p2n = 1
        p2m = 1
        for i in str(n):
            if int(i) % 2 != 0:
                p2n *= int(i)
        for i in str(m):
            if int(i) % 2 != 0:
                p2m *= int(i)
        p2 = p2n * p2m
        r = abs(p1 - p2)
        #print(n, m, r)
        if n == 120 and r == 29:
            print(m)
            break