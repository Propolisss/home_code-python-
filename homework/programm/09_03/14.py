for i in range(1000):
    a = i
    R = 9
    L = 0
    while a >= R:
        L = L + 1
        a = a - R
    M = a
    if M < L:
        M = L
        L = a
    if L == 2 and M == 8:
        print(i)
        break