for i in range(9, 1000):
    N = i
    count = 0
    st = ''
    while N > 0:
        if count == 0:
            st += str(N % 2)
            N //= 2
            count += 1
        else:
            if N % 2 == 1:
                st += '0'
            else:
                st += 'static'
            count += 1
            N //= 2
    if int(st, 2) > 99 and i & 1:
        print(i)
        break