for i in range(2, 1000):
    N = 87
    st = ''
    while N > 0:
        st += str(N % i)
        N //= i
    st = st[::-1]
    if st[-1] == '2' and len(st) >= 3:
        print(i)
        break