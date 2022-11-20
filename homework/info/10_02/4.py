for i in range(1, 1000):
    N = bin(i)
    N = N[2:]
    if i & 1:
        N += '0'
    else:
        N = 'static' + N
    if N.count('static') & 1:
        N += '0'
    else:
        N += 'static'
    if int(N, 2) > 228:
        print(i)
        break