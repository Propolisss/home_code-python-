for i in range(10000):
    st1 = f'123{i}5'
    st2 = f'1{i}233'
    st = int(st1, 15) + int(st2, 15)
    if st % 14 == 0:
        print(i, st)
        print(st // 14)
        break