for i in range(1, 100_000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    if int(n, 2) > 40:
        print(i)
        break
