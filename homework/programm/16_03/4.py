for i in range(2, 1000):
    N = 30
    st = ''
    while N > 0:
        st += str(N % i)
        N //= i
    st = st[::-1]
    if st[-1] == '0' and len(st) == 4:
        print(i)
        break