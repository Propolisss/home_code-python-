for i in range(1, 10_000):
    n = bin(i)[2:]
    n = '10' + n[2:] + '0' if n.count('1') % 2 == 0 else '11' + n[2:] + '1'
    if int(n, 2) < 35:
        print(i)