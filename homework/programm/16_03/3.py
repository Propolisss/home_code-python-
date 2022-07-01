for i in range(2, 10000):
    st = ''
    N = 30
    while N > 0:
        st += str(N % i)
        N //= i
    if len(st) == 3:
        print(i)
        break