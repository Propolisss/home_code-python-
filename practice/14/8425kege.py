def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [str(temp_n % base)] + arr
        temp_n //= base
    return arr

for p in range(3, 100):
    for x in range(1, p):
        for y in range(p):
            n1 = 3 * p + 2
            n2 = p + 4
            if (n1 * n2) == (2 + y * p + x * p ** 2):
                print(p, x, y, x + y * p)