for x in range(1, 10_000):
    if bin(4 ** 1014 - 2 ** x + 12)[2:].count('0') == 2000:
        print(x)