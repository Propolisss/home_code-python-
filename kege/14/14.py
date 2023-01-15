for x in range(2, 100_000):
    n1 = 1 * x ** 0 + 2 * x ** 1
    n2 = 3 * x ** 0 + 1 * x ** 1
    n3 = 3 * x ** 0 + 1 * x ** 1 + 3 * x ** 2
    if n1 * n2 == n3:
        print(x)