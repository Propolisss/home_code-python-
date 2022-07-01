for i in range(1, 10000):
    N = i
    n = bin(N)
    n = n[2:]
    summ = bin(n.count('1'))
    summ = summ[2:]
    if N & 1:
        n = '1' + n + '00'
    else:
        n += summ
    if int(n, 2) > 215:
        print(i)
        break