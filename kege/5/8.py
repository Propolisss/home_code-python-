for i in range(1, 10_000):
    n = bin(i * 2)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    if int(n, 2) > 1017:
        print(i)
        break