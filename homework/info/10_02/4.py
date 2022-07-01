for i in range(1, 1000):
    N = bin(i)
    N = N[2:]
    if i & 1:
        N += '0'
    else:
        N = '1' + N
    if N.count('1') & 1:
        N += '0'
    else:
        N += '1'
    if int(N, 2) > 228:
        print(i)
        break