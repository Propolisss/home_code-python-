print(2 * 4 * 4 * 4 * 2)

for i in range(1, 10000):
    n = bin(2 * i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    if int(n, 2) > 1017:
        print(i)
        break